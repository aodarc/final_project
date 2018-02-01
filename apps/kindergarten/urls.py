from django.conf.urls import url
from apps.kindergarten.views import Kindergartenview


urlpatterns = [
    url(r'^$', Kindergartenview.as_view()),
    ]