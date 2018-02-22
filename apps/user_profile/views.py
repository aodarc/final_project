# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import FormView
from apps.location.models import City
from apps.user_profile.models import Child

from apps.user_profile.forms import RegisterChildForm

class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class RegisterChildFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)





#@login_required
def child_form(request):
        cities = City.objects.all()
        #data = {
         #   'parents': request.user
        #}initial={'parents': request}
        #data.update(request.POST)
        if request.method == 'POST':
            form = RegisterChildForm(request.POST )
            if form.is_valid():
                #newform = form.save(commit=False)
                #newform.user = request.user
                form.save()
                form.parents = request.user.id
                form.save()
                #newform.save()
            #if form.is_valid():
                #form.save()
                return redirect('/user_profile/')
            return render (request, 'add_child.html', {'form' : form, 'city_list': cities})
        else:
            form = RegisterChildForm()
            return render(request, 'add_child.html', {'form' : form, 'city_list': cities})