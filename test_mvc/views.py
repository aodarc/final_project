from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def base_page(request):
    user = User.objects.last()

    context = {
        "user": user,
        "random_names": ['Alisa', "Sara", "Jessica"]
    }

    return render(
        request=request,
        template_name='base.html',
        context=context
    )
