from ast import operator
from django.db import models
blank=True

# Create your models here.
class Field(models.Model):
    field_name = models.CharField(max_length=50)
    soil_type = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"Field number: {self.field_num}"

class Crop(models.Model):
    crop_name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)
    life_form = models.CharField(max_length=50)

    def __str__(self):
        return f"Crop name: {self.crop_name}"

class Chemical(models.Model):
    chemical_type = models.CharField(max_length=50)
    date_applied = models.DateTimeField()
    chemical_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.chemical_type} applied on {self.date_applied}"