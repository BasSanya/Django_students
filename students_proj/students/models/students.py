from django.db import models
from django.utils.translation import gettext_lazy as _


class Students(models.Model):
    """Students Model"""
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("Second Name"))
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_("Surname"),
        default='')
    birthday = models.DateField(
        blank=False,
        verbose_name=_("Birthday date"),
        null=True)
    photo = models.ImageField(
        blank=True,
        verbose_name=_("Photo"),
        null=True)
    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("Ticket"))
    notes = models.TextField(
        blank=True,
        verbose_name=_("Additional notes"))
    student_group = models.ForeignKey(
        'Groups',
        verbose_name=_("Group"),
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
