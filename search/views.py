from django.shortcuts import render
from exercises.models import Exercise


# Create your views here.
def do_search(request):
    exercises = Exercise.objects.filter(name__icontains=request.Get['q'])
    return render(request, "exercises.html", {"exercises":exercises})
