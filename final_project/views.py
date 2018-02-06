from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'main_page/main_content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = "Our main page"
        return context
