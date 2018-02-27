# Register your models here.
from django.contrib import admin

from apps.kindergarten.models import (Kindergarten, Group, Queue, QueueChildRelation)

admin.site.register(Kindergarten)
admin.site.register(Group)
admin.site.register(Queue)
admin.site.register(QueueChildRelation)


class ReturnComAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'item', 'description', 'text', '_status')
