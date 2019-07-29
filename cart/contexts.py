from django.shortcuts import get_object_or_404
from exercises.models import Exercise


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    #total = 0
    #exercise_count = 0
    
    for id, quantity in cart.items():
        exercise = get_object_or_404(Exercise, pk=id)
        #total += quantity * product.price
        #exercise_count += quantity
        cart_items.append({'id': id, 'exercise': exercise})
    
    return {'cart_items': cart_items}