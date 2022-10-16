from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Field, Crop, Chemical

# Create your views here.

def field(request):
    field = get_object_or_404(Field)
    return render (request, "a/field.html", {
        "field": Field.objects.all()
    })

def crop(request):
    return render (request, "acrelog/crop.html",{
        "crop": Crop.objects.all()
    })



def index(request):
    return HttpResponse("hello world")