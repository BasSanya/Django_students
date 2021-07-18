from django.http import HttpRequest
from django.test import TestCase

from students.models import Groups
from students.util import get_current_group


class UtilsTestCase(TestCase):
    """Test function from util module"""

    def setUp(self):
        group1, created = Groups.objects.get_or_create(id=1, title='Group1')

    def test_get_current_group(self):
        request = HttpRequest()

        #  test with no group set in cookie
        request.COOKIES['current_group'] = ''
        self.assertEqual(None, get_current_group(request))

        #  test with invalid group id
        request.COOKIES['current_group'] = '1112'
        self.assertEqual(None, get_current_group(request))

        #  test with proper group identificator
        group = Groups.objects.get(title='Group1')
        request.COOKIES['current_group'] = str(group.id)
        self.assertEqual(group, get_current_group(request))

