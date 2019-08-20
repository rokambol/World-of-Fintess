from django.apps import apps
from django.test import TestCase
from .apps import FitnessProgramsConfig


class TestFitnessProgramsConfig(TestCase):

    def test_fitness_programm_app(self):
        self.assertEqual("fitness_programs", FitnessProgramsConfig.name)
        self.assertEqual("fitness_programs", apps.get_app_config("fitness_programs").name)