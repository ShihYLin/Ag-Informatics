from django.contrib import admin
from .models import Field, Crop, Chemical

# Register your models here.
admin.site.register(Field)
admin.site.register(Crop)
admin.site.register(Chemical)