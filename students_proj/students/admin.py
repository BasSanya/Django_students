from django.contrib import admin
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.forms import ModelForm


from .models import Students
from .models import Groups


class StudentFormAdmin(ModelForm):
    def clean_student_froup(self):
        group = Groups.objects.filter(leader=self.instance).first()
        if group and self.cleaned_data['student_group'] != group:
            raise ValidationError('Студент э старостою ыншоъ групи.', code='invalid')
        return self.creaned_data['student_group']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('student_update', kwargs={'pk': obj.id})


admin.site.register(Students, StudentAdmin)
admin.site.register(Groups)
