from django.conf.urls import url
from django_filters.views import FilterView

from apps.user_profile.filters import KinderFilter
from apps.user_profile.views import (
    UserProfileDetailView,
    RegisterFormView,
)
from final_project.views import MainPageView

urlpatterns = [
    url(r'^/', UserProfileDetailView.as_view()),
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
    url(r'^$', MainPageView.as_view(), name="main"),
    # url(r'^search/$', views.kinder_list, name='searcher'),
    url(r'^search/$', FilterView.as_view(filterset_class=KinderFilter, template_name='main_page/district.html'),
        name='searcher'),
]