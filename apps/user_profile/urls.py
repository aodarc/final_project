from django.conf.urls import url

from user_profile.views import (
    get_users_by_gender,
    UserProfileDetailView)

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', UserProfileDetailView.as_view()),
    url(r'^(?P<gender>[a-zA-Z]+)$', get_users_by_gender)
]
