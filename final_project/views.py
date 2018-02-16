from django.views.generic import TemplateView
from apps.kindergarten.models import Kindergarten

class MainPageView(TemplateView):
    template_name = 'main_page/main_content.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = "Our main page"
        context['kinder_list'] = Kindergarten.objects.all()
        return context

