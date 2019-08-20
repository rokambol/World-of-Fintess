from django.core.urlresolvers import resolve
from django.test import TestCase
from .forms import YourDetailsForm, MakePaymentForm
from django.http import HttpRequest
from django.conf import settings
from django.utils.module_loading import import_module
from django.template.loader import render_to_string
from django.shortcuts import render



class FormTests(TestCase):
    
    def test_make_payment_form(self):
        form = MakePaymentForm({'credit_card_number': '', 'cvv': '', 'expiry_month': ''})
        self.assertFalse(form.is_valid())


class TestDetailsForm(TestCase):
    def test_details_form(self):
        form =  YourDetailsForm({'height': '', 'weight': '', 'age': '', 'level':''})
        self.assertFalse(form.is_valid())