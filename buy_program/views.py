from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, YourDetailsForm
from django.conf import settings
from django.utils import timezone
from fitness_programs.views import fitness_program
from fitness_programs.models import fitness_programs
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

customer = stripe.Customer.create()
print(customer.last_response.request_id)

@login_required()
def buy_program(request):
    if request.method == "POST":
       #request.session.clear() # empty session dict every time function is call
       your_detailsform = YourDetailsForm(request.POST)
       if your_detailsform.is_valid():
           height= request.POST.get("height")
           weight = request.POST.get("weight")
           age = request.POST.get("age")
           level = request.POST.get("level")
           request.session["height"] = height
           request.session["weight"] = weight
           request.session["age"] = age
           request.session["level"] = level
           
           return redirect('payment')
    else:
        your_detailsform=YourDetailsForm()
    return render(request, "buy_program.html", {"your_detailsform" : your_detailsform})
    

def payment(request):
    height = int(request.session["height"])
    weight = int(request.session["weight"])
    age = int(request.session["age"])
    level = str(request.session["level"])
    if weight >= 99 and height < 180:
        table1 = fitness_programs.objects.all().filter(name="Begginer 2")
    else:
        table1 = fitness_programs.objects.all().filter(name="Begginer 1")
        
    for total in table1:
        price = total.price    
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        if payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount = int(price * 100),
                    currency="GBP",
                    payment_method_types=['card'],
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
