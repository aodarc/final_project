from django.conf.urls import url

from apps.kindergarten.views import KinderView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', KinderView.as_view()),
]