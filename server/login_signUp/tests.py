from django.test import TestCase
from django.urls import reverse


class RenderTests(TestCase):
    def test_login_view(self):
        url = reverse('api/controllers/user/login/')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_sign_up_view(self):
        url = reverse("api/controllers/user/signUp/")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_forgot_view(self):
        url = reverse("api/controllers/user/signUp/")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
