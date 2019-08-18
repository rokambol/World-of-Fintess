from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User


class TestAccountsForms(TestCase):
    def test_login_password_required(self):
        form = UserLoginForm({'username': 'admin'})
        self.assertFalse(form.is_valid())
        print(form.errors['password'], ['This field is required.'])

    def test_login_username_required(self):
        form = UserLoginForm({'password': 'dfghj'})
        self.assertFalse(form.is_valid())
        print(form.errors['username_or_email'], ['This field is required.'])

    def test_registration_passwords_must_match(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word2'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Passwords do not match'])

    def test_registration_passwords_match(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word1'
        })
        self.assertTrue(form.is_valid())

    def test_login_form(self):
        form = UserLoginForm({
            'username': 'admin',
            'password': 'pa55word1'
        })
        self.assertFalse(form.is_valid())

    def test_registration_email_must_be_unique(self):
        User.objects.create_user(
            username='testuser',
            email='admin@example.com')

        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word1'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],
                         ['Email addresses must be unique.'])
                         
