from django.conf.urls import url
from django.conf.urls import url, include

from apps.kindergarten.views import Kindergartenview
from final_project.views import MainPageView

urlpatterns = [
    url(r'^$', Kindergartenview.as_view()),
]