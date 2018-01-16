# Register your models here.
from django.contrib import admin

from apps.user_profile.models import UserProfile
from apps.user_profile.models import Child

admin.site.register(UserProfile)
admin.site.register(Child)
