{"filter":false,"title":"tests.py","tooltip":"/buy_program/tests.py","undoManager":{"mark":47,"position":47,"stack":[[{"start":{"row":1,"column":0},"end":{"row":10,"column":67},"action":"insert","lines":["from django.test import TestCase","from .models import Exercise","","# Create your tests here.","class ExerciseTests(TestCase):","    \"\"\" Run test agains Exercise model\"\"\"","    ","    def test_str(self):","        test_name = Exercise(name='ex', description='exercise description')","        self.assertEqual(str(test_name), 'ex exercise description')"],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":32},"action":"remove","lines":["from django.test import TestCase"],"id":3},{"start":{"row":0,"column":32},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["e"],"id":4},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"remove","lines":["s"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":["i"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":["c"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["r"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["e"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["x"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["E"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":27},"action":"insert","lines":["payment"],"id":5}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["e"],"id":6},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["s"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["i"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["c"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["r"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["e"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["x"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["E"]}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["p"],"id":7},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["a"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["y"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["m"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["e"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["t"],"id":8}],[{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["e"],"id":9},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["m"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"remove","lines":["a"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"remove","lines":["n"]}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["h"],"id":10},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["e"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["i"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["g"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["h"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["n"],"id":11},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"remove","lines":["o"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["i"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"remove","lines":["t"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"remove","lines":["p"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"remove","lines":["i"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"remove","lines":["r"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"remove","lines":["c"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":["s"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"remove","lines":["e"]}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"remove","lines":["d"],"id":12}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["w"],"id":13},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":43},"action":"remove","lines":["we"],"id":14},{"start":{"row":8,"column":41},"end":{"row":8,"column":47},"action":"insert","lines":["weight"]}],[{"start":{"row":8,"column":70},"end":{"row":8,"column":71},"action":"insert","lines":[","],"id":15}],[{"start":{"row":8,"column":71},"end":{"row":8,"column":72},"action":"insert","lines":[" "],"id":16}],[{"start":{"row":8,"column":72},"end":{"row":8,"column":73},"action":"insert","lines":["a"],"id":17},{"start":{"row":8,"column":73},"end":{"row":8,"column":74},"action":"insert","lines":["g"]},{"start":{"row":8,"column":74},"end":{"row":8,"column":75},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":75},"end":{"row":8,"column":76},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":8,"column":75},"end":{"row":8,"column":76},"action":"remove","lines":[" "],"id":19}],[{"start":{"row":8,"column":75},"end":{"row":8,"column":76},"action":"insert","lines":["="],"id":20}],[{"start":{"row":8,"column":76},"end":{"row":8,"column":78},"action":"insert","lines":["''"],"id":21}],[{"start":{"row":8,"column":77},"end":{"row":8,"column":78},"action":"insert","lines":["3"],"id":22},{"start":{"row":8,"column":78},"end":{"row":8,"column":79},"action":"insert","lines":["0"]}],[{"start":{"row":8,"column":68},"end":{"row":8,"column":69},"action":"remove","lines":["n"],"id":23},{"start":{"row":8,"column":67},"end":{"row":8,"column":68},"action":"remove","lines":["o"]},{"start":{"row":8,"column":66},"end":{"row":8,"column":67},"action":"remove","lines":["i"]},{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"remove","lines":["t"]},{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"remove","lines":["p"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"remove","lines":["i"]},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"remove","lines":["r"]},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"remove","lines":["c"]},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"remove","lines":["s"]},{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"remove","lines":["e"]},{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"remove","lines":["d"]},{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"remove","lines":[" "]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"remove","lines":["e"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"remove","lines":["s"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"remove","lines":["i"]}],[{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"remove","lines":["c"],"id":24},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"remove","lines":["r"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["e"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"remove","lines":["x"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["e"]}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["1"],"id":25},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["2"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["4"]}],[{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"remove","lines":["x"],"id":26},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["e"]}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["1"],"id":27},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["6"]},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["9"]}],[{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"remove","lines":["9"],"id":28},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"remove","lines":["6"]}],[{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["9"],"id":29},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["9"]}],[{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"remove","lines":["x"],"id":30},{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"remove","lines":["e"]}],[{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"insert","lines":["1"],"id":31},{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"insert","lines":["9"]},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"insert","lines":["9"]}],[{"start":{"row":9,"column":65},"end":{"row":9,"column":66},"action":"remove","lines":["n"],"id":32},{"start":{"row":9,"column":64},"end":{"row":9,"column":65},"action":"remove","lines":["o"]},{"start":{"row":9,"column":63},"end":{"row":9,"column":64},"action":"remove","lines":["i"]},{"start":{"row":9,"column":62},"end":{"row":9,"column":63},"action":"remove","lines":["t"]},{"start":{"row":9,"column":61},"end":{"row":9,"column":62},"action":"remove","lines":["p"]},{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"remove","lines":["i"]},{"start":{"row":9,"column":59},"end":{"row":9,"column":60},"action":"remove","lines":["r"]},{"start":{"row":9,"column":58},"end":{"row":9,"column":59},"action":"remove","lines":["c"]},{"start":{"row":9,"column":57},"end":{"row":9,"column":58},"action":"remove","lines":["s"]},{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"remove","lines":["e"]},{"start":{"row":9,"column":55},"end":{"row":9,"column":56},"action":"remove","lines":["d"]},{"start":{"row":9,"column":54},"end":{"row":9,"column":55},"action":"remove","lines":[" "]}],[{"start":{"row":9,"column":53},"end":{"row":9,"column":54},"action":"remove","lines":["e"],"id":33},{"start":{"row":9,"column":52},"end":{"row":9,"column":53},"action":"remove","lines":["s"]},{"start":{"row":9,"column":51},"end":{"row":9,"column":52},"action":"remove","lines":["i"]},{"start":{"row":9,"column":50},"end":{"row":9,"column":51},"action":"remove","lines":["c"]},{"start":{"row":9,"column":49},"end":{"row":9,"column":50},"action":"remove","lines":["r"]},{"start":{"row":9,"column":48},"end":{"row":9,"column":49},"action":"remove","lines":["e"]},{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"remove","lines":["x"]},{"start":{"row":9,"column":46},"end":{"row":9,"column":47},"action":"remove","lines":["e"]}],[{"start":{"row":9,"column":46},"end":{"row":9,"column":47},"action":"insert","lines":["1"],"id":34},{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"insert","lines":["2"]},{"start":{"row":9,"column":48},"end":{"row":9,"column":49},"action":"insert","lines":["4"]}],[{"start":{"row":9,"column":49},"end":{"row":9,"column":50},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":9,"column":50},"end":{"row":9,"column":51},"action":"insert","lines":["3"],"id":36},{"start":{"row":9,"column":51},"end":{"row":9,"column":52},"action":"insert","lines":["0"]}],[{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"remove","lines":["r"],"id":37},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["t"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["s"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["i"],"id":38},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["n"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"remove","lines":["t"],"id":39},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["n"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["i"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["s"],"id":40},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["t"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"remove","lines":["t"],"id":41},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":["n"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":["e"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["m"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["y"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["a"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":35},"action":"insert","lines":["YourDetailsForm"],"id":42}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["t"],"id":43},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["n"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["e"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["m"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["y"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["a"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":35},"action":"insert","lines":["YourDetailsForm"],"id":44}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":["s"],"id":45},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["l"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["e"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["d"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["o"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["m"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["f"],"id":46},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["o"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["r"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["m"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":1},"end":{"row":10,"column":25},"action":"remove","lines":[" Create your tests here.","class ExerciseTests(TestCase):","    \"\"\" Run test agains Exercise model\"\"\"","    ","    def test_str(self):","        test_name = YourDetailsForm(height='199', weight='124', age='30')","        self.assertEqual(str(test_name), '199 124 30')","# Create your tests here."],"id":47},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["#"]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":34},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":48},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"remove","lines":["m"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":["r"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["o"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"remove","lines":["F"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"remove","lines":["s"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"remove","lines":["l"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["i"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"remove","lines":["a"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":["t"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":["e"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["D"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["r"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["u"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["o"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["Y"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":[" "]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["t"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["r"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["o"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["p"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["m"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["i"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":[" "]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["s"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["m"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["r"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["o"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["f"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["."]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":[" "]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["o"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["r"]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["f"]},{"start":{"row":0,"column":32},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":["e"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"remove","lines":["s"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["a"],"id":49},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["s"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":0},"end":{"row":1,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565800235994,"hash":"d127e2e002d5280a2b2bf02b95f1e230a07e0ab1"}