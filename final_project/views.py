from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'main_page/main_content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = "Our main page"
        return context


def my_login(request):
    if request.method == 'GET':
        return render(request, 'main_page/login_page.html')
    elif request.user is AnonymousUser:
        return HttpResponseRedirect(reverse('main'))
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

        return HttpResponseRedirect(reverse('main'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))
