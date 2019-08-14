from django.shortcuts import render
from .models import Exercise


# Create your views here.
def all_exercises(request):
    exercises= Exercise.objects.all()         
    return render(request, "exercises.html", {"exercises": exercises})
    
def single_exercise(request, exercise_id):
    single_exercise = Exercise.objects.get(pk=exercise_id)
    return render (request, "single_exercise.html", {"exercise": single_exercise})
