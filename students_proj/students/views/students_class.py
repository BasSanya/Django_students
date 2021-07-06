from django.views.generic import ListView

from ..models import Students


class StudentList(ListView):
    model = Students
    context_object_name = 'students'
    template_name = 'students/students_list_class.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_logo'] = False

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.order_by('last_name')
