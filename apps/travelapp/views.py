from django.shortcuts import render
from .models import Place, Team

# Create your views here.

def index(request):
    places = Place.objects.all()
    teams = Team.objects.all()
    return render(request, 'index.html', {'places' : places, 'teams' : teams})