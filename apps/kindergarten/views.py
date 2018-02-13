from django.views.generic import ListView
from django.views.generic.detail import DetailView

from apps.kindergarten.models import (
    Kindergarten,
    Group
)


class KinderDetailView(DetailView):
    template_name = 'kindergarten/show_kindergarten.html'
    model = Kindergarten

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        context['groups'] = Group.objects.filter(kindergarten=self.object)

        return context


class KindergartenListView(ListView):
    model = Kindergarten
    template_name = 'kindergarten/kindergarten_page.html'
    context_object_name = 'kinder_list'
    queryset = Kindergarten.objects.select_related('district').all()
