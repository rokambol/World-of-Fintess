from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import do_search
from exercises.models import Exercise
from django.http import HttpRequest
from django.utils.module_loading import import_module
from django.template.loader import render_to_string

# Create your tests here.
class SearchViewTests(TestCase):
    """ Run test agains exercises views"""
    ##def test_search_view(self):
      ####  userinput = 'exercise'
       # exercise = Exercise.objects.filter(name__icontains='exercise')
       # result = Exercise.objects.all().filter(name='exercise')
      #  self.assertEquals(userinput )