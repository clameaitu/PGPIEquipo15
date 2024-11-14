from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class AccountTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

    def test_login_valid_user(self):
        response = self.client.post(reverse('account:login'), {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertRedirects(response, reverse('account:dashboard'))

    def test_login_invalid_user(self):
        response = self.client.post(reverse('account:login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(reverse('account:register'), {
            'username': 'newuser',
            'first_name': 'New',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(User.objects.count(), 2)  # El usuario de setUp + el nuevo usuario
        self.assertTemplateUsed(response, 'account/register_done.html')


class UserTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password123'))

    def test_login_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        login = self.client.login(username='testuser', password='password123')
        self.assertTrue(login)