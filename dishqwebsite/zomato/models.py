from django.db import models

# Create your models here.


class Restaurants(models.Model):
    name = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    rating = models.CharField(max_length=1000)

