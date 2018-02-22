# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView

from apps.user_profile.forms import RegisterChildForm


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


# @login_required
def child_form(request):
    if request.method == 'POST':
        form = RegisterChildForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user_profile/')
        return render(request, 'add_child.html', {'form': form})
    else:
        form = RegisterChildForm(user=request.user)
        return render(request, 'add_child.html', {'form': form})
