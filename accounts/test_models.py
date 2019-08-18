from django.test import TestCase
from .models import FitnessUser


class TestUserTypesModel(TestCase):

    def test_register_as_fitnessUser(self):
        fitnessUser = FitnessUser(user_id='1')
        fitnessUser.save()
        self.assertEqual(fitnessUser.user_id, "1")
        