# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
