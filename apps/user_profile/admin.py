# Register your models here.
from django.contrib import admin

from apps.user_profile.models import Child
from apps.user_profile.models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Child)