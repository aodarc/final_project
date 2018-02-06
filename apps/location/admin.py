# Register your models here.
from django.contrib import admin

from apps.location.models import Country, City, District

admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
