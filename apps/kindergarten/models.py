# Create your models here.
from django.db import models

from apps.location.models import District
from apps.user_profile.models import Child
from core.models.abstract_models import BaseDjangoModel
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


class Queue(BaseDjangoModel):
    name = models.CharField(
        max_length=35
    )
    kindergarten = models.ForeignKey(
        to=Kindergarten,
        related_name='queue',
        on_delete=models.SET_NULL,
        null=True
    )
    children = models.ManyToManyField(
        to=Child,
        through='QueueChildRelation',
        related_name='queues',
    )


class QueueChildRelation(BaseDjangoModel):
    STATUS_CHOICES = (
        ('A', 'Прийнята'),
        ('W', 'На розгляді'),
        ('D', 'Відмовлено')
    )
    child = models.ForeignKey(
        to=Child
    )
    queue = models.ForeignKey(
        to=Queue,
        unique=True
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        verbose_name='Статус дитини в черзі'
    )

    class Meta:
        unique_together = ('child', 'queue')
        ordering = ('-child__privilege', 'created',)
