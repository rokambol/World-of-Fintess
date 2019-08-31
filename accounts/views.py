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


def get_program(weight, height, age, level):  #funcion determinate which fitness program user purchase
    if weight >= 70 and height < 170 and age>=20 and level == 'Begginer':
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
    return table1

@login_required
def profile(request): 
    """A view that displays the profile page of a logged in user"""
    current_user = request.user
    pk = int(current_user.id)
    try:
        us = Details.objects.get(user__exact=pk)
    except Details.DoesNotExist:
        us = None
    
    if us is not None:
        height = int(us.height)
        weight = int(us.weight)
        age = int(us.age)
        level = str(us.level)
        table1 = get_program(weight, height, age, level)
    else:
        messages.info(request, "You did'n purchase any program yet!")
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
