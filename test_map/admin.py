from django.contrib import admin

# Register your models here.
from test_map.models import (
    ArticleM,
    TagM,
    Picture
)

admin.site.register(ArticleM)
admin.site.register(TagM)
admin.site.register(Picture)