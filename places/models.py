from django.db import models

from cities.models import City


class Hotel(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    photo = models.ImageField()
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Room(models.Model):
    title = models.CharField(max_length=100)
    number_of_guests = models.PositiveSmallIntegerField()
    description = models.TextField()
    photo = models.ImageField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
