from django.test import TestCase

from .models import ToDo

class IndexViewTest(TestCase):

    def test_index_view(self):

        # Create a ToDo item in the database
        ToDo.objects.create(todo_text="JFDI")

        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/index.html')
        self.assertIsNotNone(response.context['latest_todo_list'])
        self.assertTrue(response.context['latest_todo_list'].count() == 1)

    def test_add_view(self):
        response = self.client.get('/todo/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add.html')

