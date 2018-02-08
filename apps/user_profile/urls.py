from django.conf.urls import url

from apps.user_profile.views import (
    get_users_by_gender,
    UserProfileDetailView,
    RegisterFormView,
    child_form)
from final_project.views import MainPageView

urlpatterns = [
    url(r'^/', UserProfileDetailView.as_view()),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^(?P<gender>[a-zA-Z]+)$', get_users_by_gender),
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
    url(r'^$', MainPageView.as_view(), name="main"),
    url(r'^register_child$', child_form),
]