from django.test import TestCase
from django.urls import reverse


class RenderTests(TestCase):
    def login_view(self):
        url = reverse('api/controllers/user/login/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
