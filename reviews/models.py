from django.db import models
from places.models import Hotel


class Review(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date"]
