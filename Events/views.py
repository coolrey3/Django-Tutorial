from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.

# calendar --> index
def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events' : events})


def new(request):
    return  HttpResponse(' Add a new event!')


