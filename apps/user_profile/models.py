# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from apps.location.models import City
from core.models.helpers import image_path
from . import constants


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
    user = models.OneToOneField(
        to=User,
        related_name='profile'
    )
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
    PRIVILEGE_CHOICES = (
        (0, "---"),
        (1, constants.INVALID_CHILD),
        (1, constants.INVALID_CHILD_WITHOUT_CONTRAINDICATION),
        (1, constants.MILITARY_CHILD),
        (1, constants.ECO_CHILD),
        (1, constants.ORPHANS_CHILD)
    )
    privilege = models.PositiveIntegerField(
        default=0,
        choices=PRIVILEGE_CHOICES,
        verbose_name='Тип пільги дитини'
    )

    first_name = models.CharField(
        max_length=20,
        blank=False,
        verbose_name="Введіть ім'я",
    )
    last_name = models.CharField(
        max_length=40,
        blank=False,
        verbose_name="Введіть прізвище",
    )
    sure_name = models.CharField(
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

    city = models.ForeignKey(
        to=City,
        null=True,
        default=None,
    )

    street = models.CharField(
        verbose_name='Вулиця',
        max_length=100,
        null=True,
        default=None,
    )

    house = models.PositiveIntegerField(
        verbose_name='Будинок',
        null=True,
        default=None,
    )

    flat = models.PositiveIntegerField(
        verbose_name='Номер квартири',
        null=True,
        default=None,
    )

    birth_sertificate_series = models.CharField(
        verbose_name='Серія свідотства про народження',
        max_length=100,
        null=True,
        default=None,

    )

    birth_sertificate_number = models.PositiveIntegerField(
        verbose_name='Номер свідотства',
        null=True,
        default=None,

    )

    birth_sertificate = models.CharField(
        verbose_name="Дані документу",
        max_length=255,
        null=True,
        default=None,

    )

    privilege_series = models.CharField(
        verbose_name='Серія документа',
        max_length=100,
        null=True,
        default=None,
    )

    privilege_number = models.PositiveIntegerField(
        verbose_name='Номер документа',
        null=True,
        default=None,
    )

    parents = models.ForeignKey(
        to=User,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Профіль дитини'
        verbose_name_plural = 'Профілі дітей'