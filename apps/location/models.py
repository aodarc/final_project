# Create your models here.
from django.db import models
from apps.kindergarten.models import Kindergarten





class Address(models.Model):
    country = models.CharField(
        unique= True,
        max_length=255,
        blank=False,
        verbose_name='Країна'
    )

    city = models.CharField(
        unique= True,
        max_length=122,
        blank=False,
        verbose_name='Місто'
    )
    town = models.OneToOneField(to=Kindergarten)
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Місцезнаходження дитячого садка'


class District(models.Model):


    district = models.CharField(
        max_length= 22,
        blank=False,
        verbose_name='Район'
    )
    street = models.CharField(
        max_length= 122,
        blank=False,
        verbose_name='Вулиця'
    )
    region = models.ForeignKey(
        to = Address,
        related_name='district'
    )

