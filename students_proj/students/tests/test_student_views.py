from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from students.models import Students, Groups

class TestStudentList(TestCase):
    def setUp(self):
        group1, created = Groups.objects.get_or_create(title='MtM-1')
        group2, created = Groups.objects.get_or_create(title='MtM-2')

        Students.objects.get_or_create(
            first_name='Vitaliy',
            last_name="Podoba",
            birthday=datetime.today(),
            ticket='125',
            student_group=group1
        )
        Students.objects.get_or_create(
            first_name='Dmytro',
            last_name="Litvinov",
            birthday=datetime.today(),
            ticket='1258',
            student_group=group2
        )
        Students.objects.get_or_create(
            first_name='Sem',
            last_name="Stefor",
            birthday=datetime.today(),
            ticket='515',
            student_group=group1
        )
        Students.objects.get_or_create(
            first_name='Jonn',
            last_name="Drosil",
            birthday=datetime.today(),
            ticket='105',
            student_group=group2
        )

        self.url = reverse('home')

    def test_students_list(self):
        # make request to the server to get homepage
        response = self.client.get(self.url)

        # have we received OK status from the server?
        self.assertEqual(response.status_code, 200)

        # do we have student name on a page?
        self.assertContains(response, 'Vitaliy')

        # # do we have link to student edit form?
        # student_id = Students.objects.first().id
        # student_edit_link = reverse('students_edit', kwargs={'pk': student_id})
        # self.assertContains(response, student_edit_link)

        # ensure we got 3 students, pagination limit is 3
        self.assertEqual(len(response.context['students']), 3)

    # def test_order_by(self):
    #     response = self.client.get(self.url, {'order_by': 'last_name'})
    #
    #     students = response.context['students']
    #     self.assertEqual(students[0].last_name, 'Drosil')
    #     self.assertEqual(students[1].last_name, 'Litvinov')
    #     self.assertEqual(students[2].last_name, 'Podoba')
