from django.db import models

# Create your models here.
class Tag(BaseDjangoModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Article(BaseDjangoModel):
    title = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Title'
    )
    body = models.TextField(
        max_length=4000,
        verbose_name='Article body'
    )

    stars = models.FloatField(
        verbose_name="Rating",
        default=0.0
    )

    picture = models.ForeignKey(to='Picture')

    tags = models.ManyToManyField(to=Tag)


class Picture(BaseDjangoModel):
    image = models.ImageField()

    def __str__(self):
        return 'ImageID: {}'.format(self.pk)