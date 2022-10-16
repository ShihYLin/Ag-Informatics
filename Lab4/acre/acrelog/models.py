from django.db import models

# Create your models here.
class Field(models.Model):
    field_num = models.IntegerField()
    soil_type = models.CharField(max_length=20)
    fallow = models.BooleanField()

    def __str__(self):
        return f"Field number: {self.field_num}"

class Crop(models.Model):
    crop_name = models.CharField(max_length=50)
    date_planted = models.DateTimeField()
    date_harvest = models.DateTimeField()

    def __str__(self):
        return f"Crop name: {self.crop_name}"

class Chemical(models.Model):
    chemical_type = models.CharField(max_length=50)
    date_applied = models.DateTimeField()
    amount = models.FloatField()

    def __str__(self):
        return f"{self.amount} pounds of {self.chemical_type} applied on {self.date_applied}"