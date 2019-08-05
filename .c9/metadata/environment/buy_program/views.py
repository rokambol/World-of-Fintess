{"filter":false,"title":"views.py","tooltip":"/buy_program/views.py","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":35},"action":"remove","lines":["from django.shortcuts import render"],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["# Create your views here."],"id":3},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":60,"column":145},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .forms import MakePaymentForm, OrderForm","from .models import OrderLineItem","from django.conf import settings","from django.utils import timezone","from products.models import Product","import stripe","","# Create your views here.","stripe.api_key = settings.STRIPE_SECRET","","","@login_required()","def checkout(request):","    if request.method == \"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            prder.date = timezone.now()","            order.save()","","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order=order,","                    product=product,","                    quantity=quantity","                )","                order_line_item.save()","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('products'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})"]}],[{"start":{"row":3,"column":34},"end":{"row":3,"column":45},"action":"remove","lines":[", OrderForm"],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":33},"action":"remove","lines":["from .models import OrderLineItem"],"id":5},{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":44},"action":"remove","lines":["order_form = OrderForm(request.POST)"],"id":6},{"start":{"row":16,"column":4},"end":{"row":16,"column":8},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":15,"column":32},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":7}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":36},"action":"remove","lines":["order_form.is_valid() and"],"id":8},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"remove","lines":[" "]}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":49},"action":"remove","lines":["order = order_form.save(commit=False)"],"id":9}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["p"],"id":10}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["0"],"id":11}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["0"],"id":12}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["O"],"id":13}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["O"],"id":14}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["o"],"id":15}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":12},"action":"remove","lines":["    "],"id":16},{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":18,"column":35},"end":{"row":19,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":6},"end":{"row":32,"column":38},"action":"remove","lines":["  if payment_form.is_valid():","            order.date = timezone.now()","            order.save()","","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order=order,","                    product=product,","                    quantity=quantity","                )","                order_line_item.save()"],"id":17},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"remove","lines":[" "]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"remove","lines":[" "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"remove","lines":["",""],"id":18},{"start":{"row":16,"column":52},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":8},"end":{"row":18,"column":12},"action":"remove","lines":["    "],"id":19}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":20},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":52},"end":{"row":17,"column":4},"action":"remove","lines":["","    "]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":21},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":22},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":40},"action":"remove","lines":["amount=int(total * 100),"],"id":23},{"start":{"row":19,"column":12},"end":{"row":19,"column":16},"action":"remove","lines":["    "]},{"start":{"row":19,"column":8},"end":{"row":19,"column":12},"action":"remove","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":18,"column":44},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":24}],[{"start":{"row":37,"column":7},"end":{"row":37,"column":32},"action":"remove","lines":[" order_form = OrderForm()"],"id":25},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":[" "]},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":[" "]},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"remove","lines":[" "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "]},{"start":{"row":36,"column":40},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":38,"column":46},"end":{"row":38,"column":70},"action":"remove","lines":["order_form\": order_form,"],"id":26},{"start":{"row":38,"column":45},"end":{"row":38,"column":46},"action":"remove","lines":["\""]}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"remove","lines":["t"],"id":27},{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"remove","lines":["u"]},{"start":{"row":38,"column":33},"end":{"row":38,"column":34},"action":"remove","lines":["o"]},{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"remove","lines":["k"]},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"remove","lines":["c"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"remove","lines":["e"]},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"remove","lines":["h"]},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"remove","lines":["c"]}],[{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["b"],"id":28},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"insert","lines":["u"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"insert","lines":["y"]}],[{"start":{"row":38,"column":28},"end":{"row":38,"column":31},"action":"remove","lines":["buy"],"id":29},{"start":{"row":38,"column":28},"end":{"row":38,"column":39},"action":"insert","lines":["buy_program"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["t"],"id":30},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["u"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["o"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["k"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["c"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["e"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["h"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["b"],"id":31},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["u"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["t"],"id":32}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["y"],"id":33}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":7},"action":"remove","lines":["buy"],"id":34},{"start":{"row":14,"column":4},"end":{"row":14,"column":15},"action":"insert","lines":["buy_program"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["s"],"id":35},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["t"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["c"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["u"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["d"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["o"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["r"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["p"]}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["e"],"id":36}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":28},"action":"remove","lines":["from e.models import Product"],"id":37},{"start":{"row":5,"column":33},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":300,"scrollleft":0,"selection":{"start":{"row":5,"column":33},"end":{"row":5,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564780875116,"hash":"ac5d17418684beea772af1e58ad4befd9777329c"}