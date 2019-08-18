from django.apps import apps
from django.test import TestCase
from .apps import ExerciseConfig


class TestExerciseConfig(TestCase):

    def test_checkout_app(self):
        self.assertEqual("exercise", ExerciseConfig.name)
        self.assertEqual("exercises", apps.get_app_config("exercises").name)