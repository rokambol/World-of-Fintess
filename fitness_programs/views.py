from django.shortcuts import render, redirect
from .models import fitness_programs
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings


# Create your views here.
@login_required()
def fitness_program(request):
    height = int(request.session["height"])
    weight = int(request.session["weight"])
    age = int(request.session["age"])
    level = str(request.session["level"])
    if weight >= 99 and height < 180:
        table1 = fitness_programs.objects.all().filter(name="Begginer 2")
    else:
        table1 = fitness_programs.objects.all().filter(name="Begginer 1")
    return render(request, "fitness_program.html", {"table1" : table1})
    
def __str__(self):
    return '%s %s %s %s' % (self.height, self.weight, self.age, self.level)
