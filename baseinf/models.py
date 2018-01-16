from django.db import models

# Create your models here.

class City(models.Model):
    name=models.CharField(max_length=100)
    lan=models.FloatField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    Last_name = models.CharField(max_length=100)
    age=models.IntegerField()
    phone = models.CharField(max_length=15)
    city_id=models.ManyToManyField(City)
    street = models.CharField(max_length=200)
    country_id = models.ManyToManyField(Country)

    def __str__(self):
        return self.Last_name
