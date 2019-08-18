from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import all_exercises, single_exercise
from .models import Exercise
from django.http import HttpRequest
from django.conf import settings
from django.utils.module_loading import import_module
from django.template.loader import render_to_string



# Create your tests here.
class ValidHtmlTests(TestCase):

    def test_returns_valid_html_all_exercise(self):
        request = HttpRequest() 
        response = all_exercises(request) 
        self.assertTrue(response.content.startswith(b'\n<!DOCTYPE html>\n'))
        self.assertIn(b'<title>Fitness World</title>\n', response.content) 
        self.assertTrue(response.content.endswith(b'</html>'))
       
    def test_returns_correct_html_all_exercise(self):
        request = HttpRequest()
        response = all_exercises(request)
        expected_html = render_to_string('exercises.html')
        self.assertEqual(response.content.decode(), expected_html)
        
      
    #def test_returns_valid_html_single_exercise(self):
        #request = HttpRequest() 
        
       # response = single_exercise(request, 1) 
        #self.assertTrue(response.content.startswith(b'\n<!DOCTYPE html>\n'))
        #self.assertIn(b'<title>Fitness World</title>\n', response.content) 
        #self.assertTrue(response.content.endswith(b'</html>'))
       
   # def test_returns_correct_html_single_exercise(self):
      #  request = HttpRequest()
       # response = single_exercise(request, 1)
       ## expected_html = render_to_string('single_exercise.html')
       # self.assertEqual(response.content.decode(), expected_html)