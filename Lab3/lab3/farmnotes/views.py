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
    observation = field.observation_set.all()
    return render(request, 'farmnotes/notes.html', {'field': field, 'observation':observation})

#View the details of a single observation
def observation(request, field_id, observation_id):
    field_observation = get_object_or_404(Observation, pk=observation_id)
    return render(request, 'farmnotes/notes.html',{'observation': observation})
#        return HttpResponse("You're looking at observation %s related to field %s." % (observation_id, field_id))

#Show all the fields in my farm
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)
