from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..models import Students


class StudentDeleteView(DetailView):
    model = Students
    template_name = 'students/students_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return f'{reverse("home")}?status_message=Студента успішно видалено!'
