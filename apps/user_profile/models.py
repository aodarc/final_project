# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from core.models.helpers import image_path


class UserProfile(models.Model):
    SEX_CHOICES = (
        ('F', 'female'),
        ('M', 'male')
    )

    avatar = models.ImageField(
        upload_to=image_path,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Адреса'
    )
    user = models.OneToOneField(to=User)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        blank=False,
        verbose_name='Стать'
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
        unique=True,
        verbose_name='Номер телефону'
    )

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Профіль користувача'
        verbose_name_plural = 'Профілі користувачів'


class Child(models.Model):
    SEX_CHOICES = (
        ('F', 'female'),
        ('M', 'male')
    )

    firstname = models.CharField(
        max_length=20,
        blank=False,
        verbose_name="Введіть ім'я",
    )
    lastname = models.CharField(
        max_length=40,
        blank=False,
        verbose_name="Введіть прізвище",
    )
    surename = models.CharField(
        max_length=20,
        blank=False,
        verbose_name="Введіть по-батькові",
    )
    dob = models.DateField(
        max_length=4,
        blank =False,
        verbose_name= "вік дитини",
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        blank=False,
        verbose_name='Стать'
    )
    parents = models.ForeignKey(
        to=User,
        related_name='children',
        null=True
    )
    class Meta:
        verbose_name = 'Профіль користувача'
        verbose_name_plural = 'Профілі користувачів'