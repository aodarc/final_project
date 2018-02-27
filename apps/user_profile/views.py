# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from apps.user_profile.forms import SignUpForm
from apps.user_profile.models import UserProfile, Child


class UserPageView(DetailView):
    template_name = 'user_profile/user_page.html'
    model = UserProfile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['children'] = Child.objects.filter(parents=self.object)

        return context


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'main_page/signup.html', {'form': form})
