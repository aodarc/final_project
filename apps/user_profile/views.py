# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from apps.kindergarten.models import Kindergarten
from apps.user_profile.filters import KinderFilter
from apps.user_profile.models import UserProfile


def kinder_list(request):
    kinder = Kindergarten.objects.all()
    filter = KinderFilter(request.GET, queryset=kinder)
    return render(request, 'main_page/district.html', {'filter': filter})


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


#
class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
