{"filter":false,"title":"test_forms.py","tooltip":"/buy_program/test_forms.py","ace":{"folds":[],"scrolltop":60,"scrollleft":0,"selection":{"start":{"row":21,"column":41},"end":{"row":21,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":32,"mode":"ace/mode/python"}},"hash":"aee573e439c1396c4b3cf2cc87f2f9f9c6329717","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["from django.core.urlresolvers import resolve","from django.test import TestCase","from .forms import YourDetailsForm, MakePaymentForm","from django.http import HttpRequest","from django.conf import settings","from django.utils.module_loading import import_module","from django.template.loader import render_to_string","from django.shortcuts import render","","","","class FormTests(TestCase):","    ","    def test_make_payment_form(self):","        form = MakePaymentForm({'credit_card_number': '', 'cvv': '', 'expiry_month': ''})","        self.assertFalse(form.is_valid())","","","class TestDetailsForm(TestCase):","    def test_details_form(self):","        *952","        ","    ","    ","    "],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":22,"column":41},"action":"insert","lines":["from django.core.urlresolvers import resolve","from django.test import TestCase","from .forms import YourDetailsForm, MakePaymentForm","from django.http import HttpRequest","from django.conf import settings","from django.utils.module_loading import import_module","from django.template.loader import render_to_string","from django.shortcuts import render","","","","class FormTests(TestCase):","    ","    def test_make_payment_form(self):","        form = MakePaymentForm({'credit_card_number': '', 'cvv': '', 'expiry_month': ''})","        self.assertFalse(form.is_valid())","","","class TestDetailsForm(TestCase):","    def test_details_form(self):","        form =  YourDetailsForm({'height': '', 'weight': '',","                          'age': '', 'level':''})","        self.assertFalse(form.is_valid())"],"id":3}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":[" "],"id":4},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":[" "]},{"start":{"row":21,"column":20},"end":{"row":21,"column":24},"action":"remove","lines":["    "]},{"start":{"row":21,"column":16},"end":{"row":21,"column":20},"action":"remove","lines":["    "]},{"start":{"row":21,"column":12},"end":{"row":21,"column":16},"action":"remove","lines":["    "]},{"start":{"row":21,"column":8},"end":{"row":21,"column":12},"action":"remove","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":20,"column":60},"end":{"row":21,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":20,"column":60},"end":{"row":20,"column":61},"action":"insert","lines":[" "],"id":6}]]},"timestamp":1566245238450}