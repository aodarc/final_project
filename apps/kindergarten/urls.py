from django.conf.urls import url
from django.conf.urls import url, include

from apps.kindergarten.views import Kindergartenview
from final_project.views import MainPageView

urlpatterns = [
    url(r'^kindergarden/', include('apps.kindergarten.views')),
    url(r'^kindergarten/$', Kindergartenview.as_view()),
    url(r'^$', MainPageView.as_view(), name="main")
]