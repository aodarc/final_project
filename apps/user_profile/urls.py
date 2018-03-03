from django.conf.urls import url
from apps.user_profile.views import (
    RegisterFormView,
    UserPageView,
    child_form)

urlpatterns = [
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
    url(r'^(?P<pk>[0-9]+)/$', UserPageView.as_view(), name="user-page"),
    url(r'^register_child/$', child_form, name='register_child'),
]
