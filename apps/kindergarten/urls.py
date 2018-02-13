from django.conf.urls import url

from apps.kindergarten.views import (
    KinderDetailView,
    KindergartenListView
)

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', KinderDetailView.as_view(), name='kindergarten'),
    url(r'^$', KindergartenListView.as_view(), name='kindergartens'),
]