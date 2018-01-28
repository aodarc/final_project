# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Address(models.Model):
    DISTRICT_CHOICE = (
        ('Шевченківський'),
        ('Галицький'),
        ('Франківський'),
        ('Залізничний'),
        ('Сихівський'),
        ('Личаківський'),
        )

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
    Address = models.OneToOneField(to=country)  # how to do it better?
    district = models.CharField(
        max_length= 22,
        choices=DISTRICT_CHOICE,
        blank=False,
        verbose_name='Район'
    )
    street = models.CharField(
        max_length= 122,
        blank=False,
        verbose_name='Вулиця'
    )


    class Meta:
        ordering = ('-id',)
        verbose_name = 'Місцезнаходження дитячого садка'
