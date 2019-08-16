from django.core.urlresolvers import resolve
from django.test import TestCase
from .forms import YourDetailsForm
from django.http import HttpRequest
from django.conf import settings
from django.utils.module_loading import import_module
from django.template.loader import render_to_string
from django.shortcuts import render



class ExerciseTests(TestCase):
    def test_form_item_input_has_placeholder_and_id(self):
        form = YourDetailsForm(data={'height': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['height'],
                         ["You can't have an empty list item"]
                         )