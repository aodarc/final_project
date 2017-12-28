from django.contrib.auth.models import User
from django.shortcuts import render

from test_mvc.models import Article


# Create your views here.


def base_page(request):
    user = User.objects.last()

    context = {
        "articles": Article.objects.all(),
        "random_names": ['Alisa', "Sara", "Jessica"]
    }

    return render(
        request=request,
        template_name='test/aaa.html',
        context=context
    )
