from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, YourDetailsForm
from django.conf import settings
from django.utils import timezone
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def buy_program(request):
    if request.method == "POST":
       your_detailsform = YourDetailsForm(request.POST)
       if your_detailsform.is_valid():
           height= request.POST.get("height")
           weight = request.POST.get("weight")
           age = request.POST.get("age")
           level = request.POST.get("level")
           
           return (redirect('payment.html'))
    else:
        your_detailsform=YourDetailsForm()
    return render(request, "buy_program.html", {"your_detailsform" : your_detailsform})


total = 2
def payment(request):
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        try:
            customer = stripe.Charge.create(
                amount = int(total * 100),
                currency="GBP",
                description=request.user.email,
                card=payment_form.cleaned_data['stripe_id']
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
    
    return render(request, "payment.html", { "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
