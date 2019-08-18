from django.test import TestCase
from .models import fitness_programs

# Create your tests here.

#test again input in fitness_programs model

class Fitness_ProgramsTests(TestCase):
    """ testing again fitness_programs model"""
    def test_str(self):
        test_name = fitness_programs(name='alfa', price='27')
        self.assertEquals(str(test_name), 'alfa 27')
        
    