from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from .models import Riddle, Option


def index(request):
    return render(request, "index.html", {"latest_motrunich": Riddle.objects.order_by('-pub_date')[:5]})


class MainPageView(TemplateView):
    template_name = 'main_content.html'

class FirstPageView(TemplateView):
    template_name = 'first_page.html'
