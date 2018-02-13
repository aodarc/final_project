from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.kindergarten.models import Kindergarten
from apps.user_profile.filters import UserFilter
from apps.user_profile.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'main_page/main_content.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'main_page/signup.html', {'form': form})


class DistrictView(ListView):
    model = Kindergarten
    template_name = 'main_page/distrOne.html'
    context_object_name = 'kinder_list'


def search_kinder(request):
    kinder_list = Kindergarten.objects.all()
    filter = UserFilter(request.GET, queryset=kinder_list)
    return render(request, 'main_page/distrOne.html', {'filter': filter})
