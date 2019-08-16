{"filter":false,"title":"contexts.py","tooltip":"/cart/contexts.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":37},"action":"remove","lines":["from django.shortcuts import get_object_or_404","from exercises.models import Exercise"],"id":12}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":37},"action":"insert","lines":["from django.shortcuts import get_object_or_404","from exercises.models import Exercise","","","def cart_contents(request):","    \"\"\"","    Ensures that the cart contents are available when rendering","    every page","    \"\"\"","    cart = request.session.get('cart', {})","","    cart_items = []","    #total = 0","    #exercise_count = 0","    ","    for id, quantity in cart.items():","        exercise = get_object_or_404(Exercise, pk=id)","        #total += quantity * product.price","        #exercise_count += quantity","        cart_items.append({'id': id, 'exercise': exercise})","    ","    return {'cart_items': cart_items}"],"id":13}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["#"],"id":14}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":20},"action":"remove","lines":[", quantity"],"id":15}],[{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"remove","lines":["t"],"id":16},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"remove","lines":["r"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"remove","lines":["a"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"remove","lines":["c"]}],[{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["c"],"id":17},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["a"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["r"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"remove","lines":["#"],"id":28}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":4},"end":{"row":9,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565953562174,"hash":"4ab52a6a513f05a89513cdfa1d6d94a34e985df3"}