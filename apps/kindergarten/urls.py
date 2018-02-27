from django.conf.urls import url

from apps.kindergarten.views import (
    KinderDetailView,
    KindergartenListView,
    RegisterKidView)

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', KinderDetailView.as_view(), name='kindergarten'),
    url(r'register_kid$', RegisterKidView.as_view(), name='register_kid'),
    url(r'^ss$', KindergartenListView.as_view(), name='kindergartens'),
]