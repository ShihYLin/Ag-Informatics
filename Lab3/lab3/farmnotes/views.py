from django.shortcuts import render
from .models import Field
from .models import Observation
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import HttpResponse

#Show all the fields in my farm
#def index(request):
#    return HttpResponse("Hello, world! You're at the farmnotes index, or 'home' page.")

#List all notes related to a particular field
#def notes(request, field_id):
#    return HttpResponse("You're looking at the notes related to field %s." % field_id)
def notes(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'farmnotes/notes.html', {'field': field})

#View the details of a single observation
def observation(request, field_id, observation_id):
        return HttpResponse("You're looking at observation %s related to field %s." % (observation_id, field_id))

#Show all the fields in my farm
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)

#Show the observation in fields
def notes(request):
    latest_observations = Observation.objects.all()
    context = {'latest_observations': latest_observations}
    return render(request, 'farmnotes/notes.html', context)
