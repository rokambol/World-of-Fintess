from django.shortcuts import render, redirect
from .models import fitness_programs
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

# Create your views here.
@login_required()
def fitness_program(request):
    table1 = fitness_programs.objects.all()
    return render(request, "fitness_program.html", {"table1" : table1})


