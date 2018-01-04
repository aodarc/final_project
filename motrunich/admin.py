from django.contrib import admin

from .models import Option, Riddle

admin.site.register(Riddle)
admin.site.register(Option)