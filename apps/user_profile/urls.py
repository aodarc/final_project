from django.conf.urls import url

from apps.user_profile.views import signup

urlpatterns = [
    url(r'^register/$', signup, name="register"),
]
