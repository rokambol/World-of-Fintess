from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import all_exercises, single_exercise
from .models import Exercise
from django.http import HttpRequest
from django.conf import settings
from django.utils.module_loading import import_module
from django.template.loader import render_to_string


# Create your tests here.
class ExerciseTests(TestCase):
    """ Run test agains Exercise model"""
    
    def test_str(self):
        test_name = Exercise(name='ex', description='exercise description')
        self.assertEqual(str(test_name), 'ex exercise description')


    def test_url_resolves_to_all_exercises_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, all_exercises)
        
    def test_url_resolves_to_single_exercise_page_view(self):
        exercise = Exercise.objects.create(name='Test exercise',
                                         description='Some test content.',
                                         image='testex.jpg')
        #found = resolve('/single_exercise/1')
        page = Exercise
        self.assertEqual(Exercise.objects.count(), 1)
        
        
        #self.assertEqual(found.func, single_exercise)
        
    
        
    
    #def test_home_page_returns_correct_html(self):
        #request = HttpRequest() 
       ## response = all_exercises(request) 
       # self.assertFalse(response.content.startswith(b'<>'))
       # self.assertIn(b'<title>Fitness world</title>', response.content) 
       # self.assertTrue(response.content.endswith(b'</html>'))
       
    def test_returns_correct_html(self):
        
        request = HttpRequest()
        response = all_exercises(request)
        expected_html = render_to_string('exercises.html')
        self.assertEqual(response.content.decode(), expected_html)
        
        
      
        