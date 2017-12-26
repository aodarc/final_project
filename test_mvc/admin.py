from django.contrib import admin

from test_mvc.models import (
    Article,
    Tag,
    Picture
)

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Picture)
