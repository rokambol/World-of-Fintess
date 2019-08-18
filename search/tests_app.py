from django.apps import apps
from django.test import TestCase
from .apps import SearchConfig


class TestSearchConfig(TestCase):

    def test_search_app(self):
        self.assertEqual("search", SearchConfig.name)
        