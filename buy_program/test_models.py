from django.test import TestCase
from .models import Details


class TestDetailsModels(TestCase):

    def test_your_details(self):
        details = Details(height = '187', weight ='100',
                      age='33')
        details.save()
        self.assertEqual(details.height, "187")
        self.assertEqual(details.weight, "100")
        self.assertEqual(details.age, '33')
      