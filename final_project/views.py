from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from test_mvc.forms import LoginForm



class MainPageView(TemplateView):
    template_name = 'main_page/main_content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = "Our main page"

        return context


class TestFormsView(View):

    def get(self, request):
        context = {}

        context['title'] = "Our main page"

        return render(request, 'main_page/forms_example.html')

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            context = {'show_success_msg': form.is_valid()}
            return render(
                request,
                'main_page/forms_example.html',
                context=context
            )

        return render(request, 'main_page/forms_example.html')

