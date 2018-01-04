from django.conf.urls import url

from . import views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.MainPageView.as_view()),
    url(r'^first/$', views.FirstPageView.as_view()),
]