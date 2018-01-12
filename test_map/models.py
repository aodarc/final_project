from django.db import models

from core.models.abstract_models import BaseDjangoModel

# Create your models here.
class TagM(BaseDjangoModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class ArticleM(BaseDjangoModel):
    title = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Title'
    )
    body = models.TextField(
        max_length=4000,
        verbose_name='ArticleM body'
    )

    stars = models.FloatField(
        verbose_name="Rating",
        default=0.0
    )

    picture = models.ForeignKey(to='Picture')

    tags = models.ManyToManyField(to=TagM)


class Picture(BaseDjangoModel):
    image = models.ImageField()

    def __str__(self):
        return 'ImageID: {}'.format(self.pk)