from django.shortcuts import render
from django.http import HttpResponse
from .models import Field, Tillage, Install, Fertilizer, Treatment, Harvest, Terminate, Planting
from django.shortcuts import get_object_or_404

def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'acrelog/index.html', context)

def fields(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'acrelog/fields.html', {'field': field})