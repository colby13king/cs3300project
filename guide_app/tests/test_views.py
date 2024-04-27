from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'guide_app/index.html')