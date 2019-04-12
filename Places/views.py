from django.shortcuts import render
from django.http import HttpResponse
from .models import Places

# Create your views here.

# calendar --> index


def index(request):
    places = Places.objects.all()
    return render(request, 'index_places.html', {'places': places})


def new(request):
    return HttpResponse(' Add a new Place!')


