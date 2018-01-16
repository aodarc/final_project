# Create your models here.
from django.db import models

from core.models.helpers import image_path


class Kindergarden(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(
        upload_to=image_path,
        blank=True
    )
    disctict=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    advantages=models.TextField()
    groups = models.ManyToManyField("Group")

    def __str__(self):
        return self.name


class Group(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name



