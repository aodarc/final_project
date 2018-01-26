from django.conf.urls import url

from apps.user_profile.views import RegisterFormView
from apps.user_profile.views import (
    get_users_by_gender,
    UserProfileDetailView,
)

urlpatterns = [
    url(r'^/', UserProfileDetailView.as_view()),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^(?P<gender>[a-zA-Z]+)$', get_users_by_gender)
]