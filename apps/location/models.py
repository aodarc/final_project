# Create your models here.
from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=40
    )
    city = models.ForeignKey(
        to=Country,
        related_name='cities'
    )

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,
        null=False
    )


