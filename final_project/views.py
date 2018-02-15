from django.views.generic import TemplateView

from apps.user_profile.forms import RegisterChild


class MainPageView(TemplateView):
    template_name = 'main_page/main_content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['title'] = "Our main page"

        if self.request.user.is_authenticated():
            context['modal_form'] = RegisterChild()

        return context

