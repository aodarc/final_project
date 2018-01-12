from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from test_map.models import ArticleM
from test_map.forms_map import LoginFormMap



# Create your views here.

class TestFormsView(View):

    def get(self, request):
        context = {}

        context['title'] = "Our main page"

        return render(request, 'test_map/form_map.html')

    def post(self, request):
        form = LoginFormMap(data=request.POST)

        if form.is_valid():
            context = {'show_success_msg': form.is_valid()}
            return render(
                request,
                'test_map/form_map.html',
                context=context
            )

        return render(request, 'test_map/form_map.html')

