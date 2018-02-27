from django.conf.urls import url

from apps.user_profile.views import (
    UserPageView,
)

urlpatterns = [

    url(r'^(?P<pk>[0-9]+)/$', UserPageView.as_view(), name="user-page"),
]
