from django.apps import apps
from django.test import TestCase
from .apps import BuyProgramConfig


class TestBuyProgramConfig(TestCase):

    def test_buy_program_app(self):
        self.assertEqual("buy_program", BuyProgramConfig.name)
        self.assertEqual("buy_program", apps.get_app_config("buy_program").name)
        