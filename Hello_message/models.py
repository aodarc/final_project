from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='First_name')
    age        = models.BigIntegerField(verbose_name='Age')
    phone      = models.BigIntegerField(verbose_name='Phone')
    city       = models.ForeignKey(to='City')
    stret      = models.CharField(max_length=50, verbose_name='Stret')
    contry_id  = models.ForeignKey(to='Contry_id')


class Contry_id(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    area = models.BigIntegerField(verbose_name='Area')

class City(models.Model):
    name           = models.CharField(max_length=20, verbose_name='Name')
    area           = models.BigIntegerField(max_length=20, verbose_name='Area')
    biggest_street = models.CharField(max_length=20, verbose_name='Biggest street')


# Create your models here.
