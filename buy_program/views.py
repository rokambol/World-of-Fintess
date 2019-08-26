from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Details
from .forms import MakePaymentForm, YourDetailsForm
from django.conf import settings
from django.utils import timezone
from fitness_programs.views import fitness_program
from fitness_programs.models import fitness_programs
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

#customer = stripe.Customer.create()
#print(customer.last_response.request_id)

@login_required()
def buy_program(request):
    if request.method == "POST":
       #request.session.clear() # empty session dict every time function is call
       your_detailsform = YourDetailsForm(request.POST)
       if your_detailsform.is_valid():
           detail = your_detailsform.save(commit=False)
           detail.user = request.user
           detail.save()
           
           return redirect('payment')
    else:
        your_detailsform=YourDetailsForm()
    return render(request, "buy_program.html", {"your_detailsform" : your_detailsform})
    

def payment(request):
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
        
    for total in table1:
        price = total.price    
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        if payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount = int(price * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.success(request, "You have successfully paid")
                return redirect('fitness_program')
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
    return render(request, "payment.html", { "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE, "table1":table1})
