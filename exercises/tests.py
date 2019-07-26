from django.test import TestCase
from .models import Exercise

# Create your tests here.
class ExerciseTests(TestCase):
    """ Run test agains Exercise model"""
    
    def test_str(self):
        test_name = Exercise(name='ex')
        self.assertNotEqual(str(test_name), 'args')
        
        