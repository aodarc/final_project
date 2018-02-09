from django.views.generic import ListView


from apps.kindergarten.models import Kindergarten


class Kindergartenview(ListView):
    model= Kindergarten
    template_name = 'kindergarden/kindergarten_page.html'
    context_object_name = 'kinder_list'
    queryset = Kindergarten.objects.select_related('district').all()