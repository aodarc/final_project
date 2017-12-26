from django.shortcuts import render

# Create your views here.
from test_mvc.models import Article


def base_page(request):
    # user = User.objects.last()

    context = {
        "articles": Article.objects.all(),
        "random_names": ['Alisa', "Sara", "Jessica"]
    }

    return render(
        request=request,
        template_name='base.html',
        context=context
    )
