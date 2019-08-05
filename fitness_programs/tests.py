from django.test import TestCase
from .models import Fitness_Programs

# Create your tests here.

class Fitness_ProgramsTests(TestCase):
    """ testing again fitness_programs model"""
    def test_str(self):
        test_name = Fitness_Programs(day1='alfa', day2='beta')
        self.assertEquals(str(test_name), 'alfa beta')