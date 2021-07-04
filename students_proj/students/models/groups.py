from django.db import models


class Groups(models.Model):
    """Groups Model"""
    title = models.CharField(
        max_length=256,
        verbose_name='Назва'
    )

    leader = models.OneToOneField(
        'Students',
        verbose_name='Староста',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    notes = models.TextField(
        blank=True,
        verbose_name='додатковы нотатки'
    )

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

    def __str__(self):
        if self.leader:
            return "%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return "%s" % (self.title,)
