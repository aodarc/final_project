from django.conf.urls import url

from apps.user_profile.views import (
    RegisterFormView,
    UserPageView,
)

urlpatterns = [
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
    url(r'^(?P<pk>[0-9]+)/$', UserPageView.as_view(), name="user-page"),
]
