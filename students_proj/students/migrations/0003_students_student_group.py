# Generated by Django 3.2.5 on 2021-07-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20210704_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.groups', verbose_name='Група'),
        ),
    ]