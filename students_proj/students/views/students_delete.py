from django.urls import reverse
from django.views.generic import DetailView

from ..models import Students


class StudentDeleteView(DetailView):
    model = Students
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return f'{reverse("home")}?status_message=Студента успішно видалено!'
