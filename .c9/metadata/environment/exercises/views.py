{"changed":true,"filter":false,"title":"views.py","tooltip":"/exercises/views.py","value":"from django.shortcuts import render\nfrom .models import Exercise\n\n\n# Create your views here.\ndef all_exercises(request):\n    exercises= Exercise.objects.all()\n    return render(request, \"exercises.html\", {\"exercises\": exercises})\n    \ndef single_exercise(request):\n    return render(request, \"single_exercise.html\")\n","undoManager":{"mark":12,"position":41,"stack":[[{"start":{"row":7,"column":43},"end":{"row":7,"column":69},"action":"remove","lines":[", {\"exercises\": exercises}"],"id":4}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":44},"action":"remove","lines":["return render(request, 'exercises.html')"],"id":6}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":67},"action":"insert","lines":["return render(request, \"products.html\", {\"products\": products})"],"id":7}],[{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"remove","lines":["s"],"id":9},{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"remove","lines":["t"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"remove","lines":["c"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"remove","lines":["u"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"remove","lines":["d"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"remove","lines":["o"]},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"remove","lines":["r"]},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"remove","lines":["p"]}],[{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["e"],"id":10},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["x"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":46},"end":{"row":7,"column":49},"action":"remove","lines":["exe"],"id":11},{"start":{"row":7,"column":46},"end":{"row":7,"column":55},"action":"insert","lines":["exercises"]}],[{"start":{"row":7,"column":65},"end":{"row":7,"column":66},"action":"remove","lines":["s"],"id":12},{"start":{"row":7,"column":64},"end":{"row":7,"column":65},"action":"remove","lines":["t"]},{"start":{"row":7,"column":63},"end":{"row":7,"column":64},"action":"remove","lines":["c"]},{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"remove","lines":["u"]},{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"remove","lines":["d"]},{"start":{"row":7,"column":60},"end":{"row":7,"column":61},"action":"remove","lines":["o"]},{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"remove","lines":["r"]},{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"remove","lines":["p"]}],[{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"insert","lines":["e"],"id":13},{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"insert","lines":["x"]},{"start":{"row":7,"column":60},"end":{"row":7,"column":61},"action":"insert","lines":["e"]},{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"insert","lines":["r"]},{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"insert","lines":["c"]}],[{"start":{"row":7,"column":63},"end":{"row":7,"column":64},"action":"insert","lines":["i"],"id":14},{"start":{"row":7,"column":64},"end":{"row":7,"column":65},"action":"insert","lines":["s"]},{"start":{"row":7,"column":65},"end":{"row":7,"column":66},"action":"insert","lines":["e"]},{"start":{"row":7,"column":66},"end":{"row":7,"column":67},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"remove","lines":["s"],"id":15},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"remove","lines":["t"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"remove","lines":["c"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"remove","lines":["u"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"remove","lines":["d"]}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"remove","lines":["o"],"id":16},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"remove","lines":["r"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"remove","lines":["p"]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["e"],"id":17},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["x"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["e"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["r"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["c"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["i"]}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["s"],"id":18},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["e"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":70},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["d"],"id":21},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":["e"]},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":[" "],"id":22}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["e"],"id":23},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["x"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["e"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["r"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["c"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["i"],"id":24},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["s"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["s"],"id":25},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["i"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["n"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["g"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["e"],"id":26},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":21},"action":"insert","lines":["()"],"id":27}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["r"],"id":28},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["e"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["q"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["u"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["e"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["s"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":[":"],"id":29}],[{"start":{"row":9,"column":29},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["r"],"id":31},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["e"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["t"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["n"],"id":32},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"remove","lines":["t"],"id":33}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"remove","lines":["n"],"id":34}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["r"],"id":35},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":[" "],"id":36},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["r"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["e"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["n"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["d"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["r"],"id":37}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":19},"action":"insert","lines":["()"],"id":38}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["r"],"id":39},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["e"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["q"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["u"]}],[{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["e"],"id":40},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["s"]},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":25},"end":{"row":10,"column":26},"action":"insert","lines":[","],"id":41}],[{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"insert","lines":[" "],"id":42}],[{"start":{"row":10,"column":27},"end":{"row":10,"column":29},"action":"insert","lines":["\"\""],"id":43}],[{"start":{"row":10,"column":28},"end":{"row":10,"column":29},"action":"insert","lines":["s"],"id":44},{"start":{"row":10,"column":29},"end":{"row":10,"column":30},"action":"insert","lines":["i"]},{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"insert","lines":["n"]},{"start":{"row":10,"column":31},"end":{"row":10,"column":32},"action":"insert","lines":["g"]}],[{"start":{"row":10,"column":28},"end":{"row":10,"column":32},"action":"remove","lines":["sing"],"id":45},{"start":{"row":10,"column":28},"end":{"row":10,"column":43},"action":"insert","lines":["single_exercise"]}],[{"start":{"row":10,"column":43},"end":{"row":10,"column":44},"action":"insert","lines":["."],"id":46},{"start":{"row":10,"column":44},"end":{"row":10,"column":45},"action":"insert","lines":["h"]}],[{"start":{"row":10,"column":45},"end":{"row":10,"column":46},"action":"insert","lines":["t"],"id":47},{"start":{"row":10,"column":46},"end":{"row":10,"column":47},"action":"insert","lines":["m"]},{"start":{"row":10,"column":47},"end":{"row":10,"column":48},"action":"insert","lines":["l"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":4},"end":{"row":9,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564334463603}