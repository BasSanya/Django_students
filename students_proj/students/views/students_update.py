from datetime import datetime

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView

from ..models import Students


class StudentUpdateForm(ModelForm):

    class Meta:
        model = Students
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_action = reverse('students_update', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-3 col-form-label'
        self.helper.field_class = 'col-sm-9'

        self.helper.layout.append(FormActions(
            Submit('add_button', 'Додати'),
            Submit('cancel_button', 'Скасувати', css_class='btn-danger'),
        ))


class StudentUpdateView(UpdateView):
    model = Students
    template_name = 'students/students_update.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return f'{reverse("home")}?status_message=Студента успішно збережено!'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(f'{reverse("home")}?status_message=Редагування студента відмінено!')
        else:
            return super().post(request, *args, **kwargs)
