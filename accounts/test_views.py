from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404


class TestLoginView(TestCase):

    def test_can_log_in(self):
        user1 = User.objects.create_user(
            username='testUser',
            email='testUser@example.com',
            password='passw0rd')

        response = self.client.post("/accounts/login", {
            'username': 'testUser',
            'password': 'pass0word'
        })

        response = self.client.get('/accounts/login')



class TestRegisterUserTypesView(TestCase):

    def test_invalid_form_does_not_register(self):
        response = self.client.post("/accounts/register", {
            'username': 'testUser2',
            'email': 'testUser2@example.com',
            'password1': 'pa55word',
            'password2': 'pa55word1!!',
        })
        self.assertEqual(User.objects.count(), 0)


