from django.views.generic import ListView
from django.views.generic import DetailView


from apps.kindergarten.models import Kindergarten
from apps.location.models import District


class Kindergartenview(ListView):
    model= Kindergarten
    template_name = 'main_page/kindergarten_page.html'
    context_object_name = 'kinder_list'
