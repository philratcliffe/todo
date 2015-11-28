from django.test import TestCase

from .models import ToDo

class IndexViewTest(TestCase):

    def test_index_view(self):
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/index.html')
