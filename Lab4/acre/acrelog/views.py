from django.shortcuts import render
from .models import Field, Crop, Chemical

# Create your views here.

def field(request):
    return render (request, "acrelog/field.html", {
        "field": Field.objects.all()
    })

def crop(request):
    return render (request, "acrelog/crop.html",{
        "crop": Crop.objects.all()
    })

def chemical(request):
    return render (request, "acrelog/chemical.html", {
        "chemical": Chemical.objects.all()
    })