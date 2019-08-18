from django.test import TestCase
from .models import Details
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from accounts.models import FitnessUser


class TestFitnessUserViews(TestCase):

    def test_get_checkout_page_as_fitness_user(self):
        User.objects.create_user(
            username='testUser1',
            email='testUser1@example.com',
            password='password1')
        fitness_user = FitnessUser.objects.create(user_id='1')
        self.client.login(username='testUser1', password='password1')
        page = self.client.get("/exercises/")
        self.assertEqual(page.status_code, 200)

    def test_card_accepted(self):
        User.objects.create_user(
            username='testSwimmer1',
            email='testSwimmer1@example.com',
            password='password1')
        fitness_user = FitnessUser.objects.create(user_id='1')
        self.client.login(username='testUser1', password='password1')

        response = self.client.post('/payment', {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2019',
            }, follow=True)

        for message in get_messages(response.wsgi_request):
            self.assertNotEqual('Your card was declined!', messages)


    def test_card_declined(self):

        User.objects.create_user(
            username='testUser1',
            email='testUser1@example.com',
            password='password1')
        fitness_user = FitnessUser.objects.create(user_id='1')
        self.client.login(username='testUser1', password='password1')

        response = self.client.post('/payment', {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2017',
            'stripe_id': 'tok_chargeDeclined',
            }, follow=True)

        for message in get_messages(response.wsgi_request):
            self.assertEqual('Your card was declined!', messages)
