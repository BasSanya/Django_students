from django.test import TestCase

from ..models import Students


class StudentModelTests(TestCase):

    def test_str(self):
        student = Students(first_name='Demo', last_name='Student')
        self.assertEqual(str(student), 'Demo Student')