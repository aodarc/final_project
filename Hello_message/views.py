from django.shortcuts import render


def hello_message(request):
    return render(
        request=request,
        template_name = 'my_self.html',
)
# user = User.objects.last()






