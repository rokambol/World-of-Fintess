from django.shortcuts import render, redirect
from .models import fitness_programs
from buy_program.models import Details
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings


# Create your views here.
@login_required()
def fitness_program(request):
    
    allSet = Details.objects.values()
    h = Details.objects.values('height', 'weight', 'age', 'level')[0]
    height = int(h['height'])
    weight = int(h['weight'])
    age = int(h['age'])
    level = str(h['level'])
    
    if weight == height == age:
        messages.error(request, "You have input unrealistic details")
    elif weight >200 or age > 100 or height > 220:
         messages.error(request, "You have input unrealistic details")
    elif weight < 45 or age < 16 or height < 135:
         messages.error(request, "You have input negative value or you body details are not suitible for fitness exercise yet!!!")
    elif weight >= 70 and height < 170 and age>=20 and level == 'Begginer':
        table1 = fitness_programs.objects.all().filter(name="Begginer 2")
    elif weight < 70 and height >= 170 and age<20 and level == 'Begginer':
        table1 = fitness_programs.objects.all().filter(name="Begginer 1")
    elif weight >= 70 and height < 170 and age>=20 and level == 'Medium':
        table1 = fitness_programs.objects.all().filter(name="Medium 2")
    elif weight < 70 and height >= 170 and age<20 and level == 'Medium':
        table1 = fitness_programs.objects.all().filter(name="Medium 1")
    elif weight >= 70 and height < 170 and age>=20 and level == 'Advance':
        table1 = fitness_programs.objects.all().filter(name="Advance 2")
    elif weight < 70 and height >= 170 and age<20 and level == 'Medium':
        table1 = fitness_programs.objects.all().filter(name="Advance 1")
        
    print(allSet, height, weight, age, level)
    
    return render(request, "fitness_program.html", {"table1" : table1})
    
def __str__(self):
    return '%s %s %s %s' % (self.height, self.weight, self.age, self.level)
