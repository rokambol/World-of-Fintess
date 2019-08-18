from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import do_search
from exercises.models import Exercise
from django.http import HttpRequest
from django.utils.module_loading import import_module
from django.template.loader import render_to_string

# Create your tests here.
class ExerciseViewTests(TestCase):
    """ Run test agains exercises views"""
    