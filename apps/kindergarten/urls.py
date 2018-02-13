from django.conf.urls import url

from apps.kindergarten.views import KindergartenView

urlpatterns = [
    url(r'^$', KindergartenView.as_view(), name='kinder'),
    ]