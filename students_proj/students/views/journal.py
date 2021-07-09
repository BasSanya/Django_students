from calendar import monthrange, day_abbr, weekday
from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..models import Students, MonthJournal
from ..util import paginate


class JournalView(TemplateView):
    template_name = 'students/journal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
        else:
            today = datetime.today()
            month = date(today.year, today.month, 1)

        #  for template
        next_month = month + relativedelta(months=1)
        prev_month = month - relativedelta(months=1)
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')

        #  for pagination
        context['cur_month'] = month.strftime('%Y-%m-%d')

        #  for template
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear, mmonth)[1]
        context['month_header'] = [
            {'day': d, 'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
            for d in range(1, number_of_days + 1)]

        if kwargs.get('pk'):
            queryset = [Students.objects.get(pk=kwargs['pk'])]
        else:
            queryset = Students.objects.order_by('last_name')

        update_url = reverse('journal')

        students = []
        for student in queryset:
            journal = (MonthJournal.objects.filter(student=student, date=month).first())

            days = []
            for day in range(1, 32):
                days.append(
                    {'day': day,
                     'present': journal and getattr(journal, 'present_day%d' % day, False) or False,
                     'date': date(2021, 7, day).strftime('%Y-%m-%d'),
                     })

            students.append({
                'fullname': f'{student.last_name} {student.first_name}',
                'days': days,
                'id': student.id,
                'update_url': update_url,
            })

        context = paginate(students, 10, self.request, context, var_name="students")

        return context

    def post(self, request, *args, **kwargs):
        data = request.POST

        current_data = datetime.strptime(data['date'], '%Y-%m-%d').date()

        month = date(current_data.year, current_data.month, 1)
        present = data['present'] and True or False
        student = Students.objects.get(pk=data['pk'][0])

        journal, created = MonthJournal.objects.get_or_create(student=student, date=month)

        setattr(journal, f'present_day{current_data.day}', present)
        journal.save()

        return JsonResponse({'key': 'success'})



