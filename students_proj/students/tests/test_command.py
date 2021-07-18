from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class CountStudentTest(TestCase):

    fixtures = ['students_test_data.json']

    def test_command_output(self):
        out = StringIO()

        call_command('countstudents', 'students', 'group', 'user', stdout=out)

        result = out.getvalue()

        self.assertContains('students in database: 4', result)
        self.assertContains('groups in database: 2', result)
        self.assertContains('users in database: 1', result)
