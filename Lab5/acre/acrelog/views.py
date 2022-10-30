from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Field, Crop, Chemical

# Create your views here.

#def field(request):
#    field = get_object_or_404(Field)
#    return render (request, "acrelog/field.html", {
#        "field": Field.objects.all()
#    })

#def crop(request):
#    return render (request, "acrelog/crop.html",{
#        "crop": Crop.objects.all()
#    })

#def chemical(request):
#    return render (request, "acrelog/chemical.html",{
#        "chemical": Chemical.objects.all()
#    })
    
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'acrelog/index.html', context)

# def fields(request, field_name, crop_id, chemical_id):
#     field = get_object_or_404(Field, pk=field_name)
#     crop = get_object_or_404(Crop, pk=crop_id)
#     chemical = get_object_or_404(Chemical, pk=chemical_id)
#     return render(request, 'acrelog/fields.html',{'field':field, 'crop':crop, 'chemical':chemical})

def fields(request, field_name):
    field = get_object_or_404(Field, pk=field_name)
    return render(request, 'acrelog/fields.html',{'field':field})