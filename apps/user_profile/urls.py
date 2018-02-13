from django.conf.urls import url

from apps.user_profile.views import RegisterFormView

urlpatterns = [
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
]
