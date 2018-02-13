from django.conf.urls import url

from apps.kindergarten.views import KinderView, Kindergartenview

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', KinderView.as_view(), name='show-kindergarten'),
    url(r'^$', Kindergartenview.as_view(), name='kinder'),
]