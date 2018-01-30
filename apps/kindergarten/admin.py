# Register your models here.
from django.contrib import admin

from apps.kindergarten.models import (Kindergarten, Group)

admin.site.register(Kindergarten)
admin.site.register(Group)