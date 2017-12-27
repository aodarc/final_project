from django.shortcuts import render

# Create your views here.
def index(request):
    # user = User.objects.last()

    return render(request,'my_self.html')




