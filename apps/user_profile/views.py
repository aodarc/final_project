# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from apps.user_profile.forms import RegisterChildForm
from apps.user_profile.models import UserProfile


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'main_page/main_content.html'


def get_user_profile(request, user_id=None):
    user_profile = get_object_or_404(UserProfile, pk=user_id)

    if user_profile:
        res = "<h1 align='center'>{}</h1>".format(
            user_profile.user.get_full_name()
        )
        return HttpResponse(res)
    else:
        return HttpResponse("<h1 align='center'>Not found</h1>")


def get_users_by_gender(request, gender):
    user = UserProfile.objects.filter(sex=gender).last()
    res = "<h1 align='center'>{}</h1>".format(
        user.user.get_full_name()
    )
    return HttpResponse(res)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)




def child_form(request):
    if request.method == 'POST':
        form = RegisterChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render (request, 'add_child.html', {'form' : form})
    else:

        form = RegisterChildForm()
        return render(request, 'add_child.html', {'form' : form})