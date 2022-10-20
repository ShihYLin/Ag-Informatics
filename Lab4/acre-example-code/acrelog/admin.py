from django.contrib import admin
from .models import Field, Tillage, Planting, Fertilizer, Treatment, Harvest, Terminate, Install
# Register your models here.
admin.site.register(Field)
admin.site.register(Tillage)
admin.site.register(Planting)
admin.site.register(Fertilizer)
admin.site.register(Treatment)
admin.site.register(Harvest)
admin.site.register(Terminate)
admin.site.register(Install)
