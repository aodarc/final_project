from django.views.generic import ListView


from apps.kindergarten.models import Kindergarten


class Kindergartenview(ListView):
    model= Kindergarten
    template_name = 'main_page/kindergarten_page.html'
    context_object_name = 'kinder_list'



