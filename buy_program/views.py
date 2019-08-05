from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm
from django.conf import settings
from django.utils import timezone
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def buy_program(request):
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        try:
            customer = stripe.Charge.create(
                currency="EUR",
                description=request.user.email,
                card=payment_form.cleaned_data['stripe_id']
            )
        except stripe.error.CardError:
            messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
    
    return render(request, "buy_program.html", { "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
