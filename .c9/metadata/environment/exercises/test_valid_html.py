{"filter":false,"title":"test_valid_html.py","tooltip":"/exercises/test_valid_html.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":0,"column":0},"end":{"row":26,"column":67},"action":"insert","lines":["def test_returns_valid_html_all_exercise(self):","        request = HttpRequest() ","        response = all_exercises(request) ","        self.assertTrue(response.content.startswith(b'\\n<!DOCTYPE html>\\n'))","        self.assertIn(b'<title>Fitness World</title>\\n', response.content) ","        self.assertTrue(response.content.endswith(b'</html>'))","       ","    def test_returns_correct_html_all_exercise(self):","        request = HttpRequest()","        response = all_exercises(request)","        expected_html = render_to_string('exercises.html')","        self.assertEqual(response.content.decode(), expected_html)","        ","      ","    #def test_returns_valid_html_single_exercise(self):","        #request = HttpRequest() ","        ","       # response = single_exercise(request, 1) ","        #self.assertTrue(response.content.startswith(b'\\n<!DOCTYPE html>\\n'))","        #self.assertIn(b'<title>Fitness World</title>\\n', response.content) ","        #self.assertTrue(response.content.endswith(b'</html>'))","       ","   # def test_returns_correct_html_single_exercise(self):","      #  request = HttpRequest()","       # response = single_exercise(request, 1)","       ## expected_html = render_to_string('single_exercise.html')","       # self.assertEqual(response.content.decode(), expected_html)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":7,"column":51},"action":"insert","lines":["from django.core.urlresolvers import resolve","from django.test import TestCase","from .views import all_exercises, single_exercise","from .models import Exercise","from django.http import HttpRequest","from django.conf import settings","from django.utils.module_loading import import_module","from django.template.loader import render_to_string"],"id":4}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":30},"action":"insert","lines":["# Create your tests here.","class ExerciseTests(TestCase):"],"id":5}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["e"],"id":6},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["s"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["i"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["c"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["r"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["e"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["x"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["E"]}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["V"],"id":7}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["a"],"id":8},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["l"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["i"]}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["d"],"id":9},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["H"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["m"],"id":10},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["l"]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["",""],"id":11},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":347,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":40,"column":67},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1566162338123,"hash":"deedc62187d874bc46d2d621391b5983a2716fa0"}