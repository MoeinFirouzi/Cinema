from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
