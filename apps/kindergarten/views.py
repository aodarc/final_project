from django.views.generic import DetailView

from apps.kindergarten.models import Kindergarten


class Kindergartenview(DetailView):
    model= Kindergarten
    template_name = 'main_page/kindergarten_page.html'


    def get_context_object_name(self, name):
        return self.name


