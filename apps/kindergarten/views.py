from django.shortcuts import render_to_response
from apps.kindergarten.models import (
    Kindergarten,
    Group
)
from apps.kindergarten.templates import *

from django.views.generic.detail import DetailView
from django.views.generic import ListView

class KinderView(DetailView):
    template_name = 'show_kindergarten.html'
    model = Kindergarten

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        context['groups'] = Group.objects.filter(kindergarten=self.object)

        return context


class Kindergartenview(ListView):
    model= Kindergarten
    template_name = 'kindergarden/kindergarten_page.html'
    context_object_name = 'kinder_list'
    queryset = Kindergarten.objects.select_related('district').all()
