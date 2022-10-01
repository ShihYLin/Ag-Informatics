from django.shortcuts import render
from .models import Field

# Create your views here.
from django.http import HttpResponse

#Show all the fields in my farm
def index(request):
    return HttpResponse("Hello, world! You're at the farmnotes index, or 'home' page.")

#List all notes related to a particular field
def notes(request, field_id):
    return HttpResponse("You're looking at the notes related to field %s." % field_id)

#View the details of a single observation
def observation(request, field_id, observation_id):
        return HttpResponse("You're looking at observation %s related to field %s." % (observation_id, field_id))

#Show all the fields in my farm
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)