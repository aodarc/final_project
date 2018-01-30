# Create your models here.
from django.db import models

from apps.location.models import District
from core.models.helpers import image_path


class Kindergarten(models.Model):
    name = models.CharField(
        max_length=200
    )
    image = models.ImageField(
        upload_to=image_path,
        blank=True
    )
    district = models.ForeignKey(
        to=District,
        related_name='kindergarten'
    )
    street = models.CharField(
        max_length=40,
        default='',
        verbose_name='Вулиця'
    )
    address = models.CharField(
        max_length=40,
        blank=False,
        default='',
        verbose_name='номер будинку'
    )

    advantages = models.TextField()
    groups = models.ManyToManyField("Group")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(
        max_length=200
    )
    description = models.TextField()

    def __str__(self):
        return self.name
