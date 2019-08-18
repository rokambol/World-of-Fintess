from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import all_exercises, single_exercise
from .models import Exercise
from django.http import HttpRequest
from django.conf import settings
from django.utils.module_loading import import_module
from django.template.loader import render_to_string


# Create your tests here.
class ExerciseViewTests(TestCase):
    """ Run test agains exercises views"""
    
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
        
        page = Exercise
        self.assertEqual(Exercise.objects.count(), 1)
        