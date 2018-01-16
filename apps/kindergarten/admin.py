# Register your models here.
from django.contrib import admin

from apps.kindergarten.models import Kindergarden, Group

admin.site.register(Kindergarden)
admin.site.register(Group)