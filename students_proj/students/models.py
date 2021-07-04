from django.db import models


class Students(models.Model):
    """Students Model"""
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Ім'я"
    )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Прізвище")
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="По-батькові",
        default='')
    birthday = models.DateField(
        blank=False,
        verbose_name="Дата народження",
        null=True)
    photo = models.ImageField(
        blank=True,
        verbose_name="Фото",
        null=True)
    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Білет")
    notes = models.TextField(
        blank=True,
        verbose_name="Додаткові нотатки")
    student_group = models.ForeignKey(
        'Groups',
        verbose_name='Група',
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'


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
