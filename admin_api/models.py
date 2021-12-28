from django.db import models
from django.db.models.expressions import RowRange


class  animal(models.Model):
    animalDescription = models.CharField(max_length=255)
    animalColour = models.CharField(max_length=255)
    animalAge = models.IntegerField()
    animalGender = models.CharField(max_length=128)
    animalLocation = models.CharField(max_length=255)
    animalWeight = models.IntegerField()
    animalHeight = models.IntegerField()
    animalPicture = models.CharField(max_length=600)
    animalNasal = models.CharField(max_length=128)


def __str__(self):
    return self


