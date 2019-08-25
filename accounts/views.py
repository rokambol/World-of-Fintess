from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from .models import FitnessUser
from fitness_programs.models import fitness_programs
from buy_program.models import Details
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request): 
    """A view that displays the profile page of a logged in user"""
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
   
    return render(request, 'profile.html', {"table1":table1, "height":height, "weight":weight, "age": age, "level": level})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
