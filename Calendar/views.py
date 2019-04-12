from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Places

# Create your views here.

# calendar --> index


def home(request):
    # places = Places.objects.all()
    return render(request, 'home.html')
    # {'places': places})


# def new(request):
#     return HttpResponse(' Add a new Place!')


