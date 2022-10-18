from ast import operator
from django.db import models
blank=True

# Create your models here.
class Field(models.Model):
    field_name = models.CharField(max_length=50, default='field_name')
    soil_type = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default='location')

    def __str__(self):
        return f"Field name: {self.field_name}"

class Crop(models.Model):
    crop_name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50, default='sci_name')
    life_form = models.CharField(max_length=50, default='form')

    def __str__(self):
        return f"Crop name: {self.crop_name}"

class Chemical(models.Model):
    chemical_type = models.CharField(max_length=50)
    date_applied = models.DateTimeField()
    chemical_name = models.CharField(max_length=50, default='chemical')

    def __str__(self):
        return f"{self.chemical_type} applied on {self.date_applied}"