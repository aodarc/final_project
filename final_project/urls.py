"""final_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from apps.user_profile.views import RegisterFormView
from apps.kindergarten.views import Kindergartenview
from final_project.views import MainPageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('apps.user_profile.urls')),
    url(r'^kindergarden/', include('apps.kindergarten.urls')),
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
    url(r'^kindergarden/$', Kindergartenview(), name="kindergarten_page"),
    url(r'^$', MainPageView.as_view(), name="main")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)