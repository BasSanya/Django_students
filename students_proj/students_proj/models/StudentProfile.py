from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile')

    mobile_phone = models.CharField(
        max_length=12,
        blank=True,
        verbose_name=_('Mobile Phone'),
        default=''
    )

    class Meta(object):
        verbose_name = _('User Profile')

    def __str__(self):
        return self.user.username
