from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthTests(TestCase):

    def register_and_login(self):
        self.client.post(reverse('sign-up'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'role': 'buyer'
        })
        self.client.login(username='testuser', password='TestPassword123!')

    def test_register_user(self):
        response = self.client.post(reverse('sign-up'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'SecurePass456!',
            'password2': 'SecurePass456!',
            'role': 'seller'
        })
        self.assertRedirects(response, reverse('homepage'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_success(self):
        self.register_and_login()
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertContains(response, "Invalid", status_code=200)

    def test_settings_page_loads(self):
        self.register_and_login()
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Settings')

    def test_edit_user_info(self):
        self.register_and_login()
        response = self.client.post(reverse('settings'), {
            'username': 'updateduser',
            'email': 'updated@example.com',
            'role': 'buyer'
        })
        self.assertRedirects(response, reverse('settings'))
        self.assertTrue(User.objects.filter(username='updateduser').exists())

    def test_delete_account(self):
        self.register_and_login()
        response = self.client.post(reverse('delete_account'))
        self.assertRedirects(response, reverse('login'))
        self.assertFalse(User.objects.filter(username='testuser').exists())
