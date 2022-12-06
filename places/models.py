from django.db import models

from cities.models import City


class Hotel(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

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


class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport = models.CharField(max_length=9)
    first_day = models.DateField(null=True)
    last_day = models.DateField(null=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE,)

    def __str__(self):
        return self.last_name
