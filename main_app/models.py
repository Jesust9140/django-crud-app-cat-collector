from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
