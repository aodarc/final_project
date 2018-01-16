from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request


def fp(request):
    return render (request, 'base.html')
