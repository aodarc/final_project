# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from apps.user_profile.models import UserProfile


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class UserPageView(DetailView):
    template_name = 'user_profile/user_page.html'
    model = UserProfile


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context ['children'] = Child.objects.filter(parents=self.object)

        return context
