from django.test import TestCase
from django.urls import reverse


class TestStudentUpdateForm(TestCase):
    fixtures = ['students_test_data.json']

    def setUp(self):
        self.url = reverse('students_edit', kwargs={'pk': 1})

    def test_form(self):
        self.client.login(username='admin', password='admin')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Edit Student')
        self.assertContains(response, 'Ticket')
        self.assertContains(response, 'Last Name')
        self.assertContains(response, 'name="cancel_button"')
        self.assertContains(response, 'name="add_button"')
        self.assertContains(response, f'action="{self.url}"')
        self.assertContains(response, 'Vitaliy.jpg')
