from django.shortcuts import render
from .models import Exercise


# Create your views here.
def all_exercises(request):
    exercises= Exercise.objects.all()
    return render(request, "exercises.html", {"exercises": exercises})
