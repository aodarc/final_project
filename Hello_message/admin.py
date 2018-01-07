from django.contrib import admin

# Register your models here.
from Hello_message.models import (
    User,
    City,
    Contry_id
)

admin.site.register(User)
admin.site.register(City)
admin.site.register(Contry_id)
