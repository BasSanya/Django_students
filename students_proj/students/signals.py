import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Students


@receiver(post_save, sender=Students)
def log_student_updated_added_event(sender, **kwargs):
    """"Writes information about newly added or updated student into log file"""
    log = logging.getLogger(__name__)

    student = kwargs['instance']
    if kwargs['created']:
        log.info(f'Student added: {student.first_name} {student.last_name} (ID: {student.id})')
    else:
        log.info(f'Student updated: {student.first_name} {student.last_name} (ID: {student.id})')

@receiver(post_delete, sender=Students)
def log_student_delete_event(sender, **kwargs):
    """Writes information about deleted student into log file"""
    log = logging.getLogger(__name__)

    student = kwargs['instance']
    log.info(f'Student deleted: {student.first_name} {student.last_name} (ID: {student.id})')
