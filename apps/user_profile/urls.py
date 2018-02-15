from django.conf.urls import url

from apps.user_profile.views import (
    RegisterFormView,
    child_form)
from final_project.views import MainPageView

urlpatterns = [
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
    url(r'^$', MainPageView.as_view(), name="main"),
    url(r'^register_child$', child_form),
]