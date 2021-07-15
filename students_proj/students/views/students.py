from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _

from ..models import Students, Groups
from ..util import get_current_group, paginate


def students_list(request):
    current_group = get_current_group(request)
    if current_group:
        students = Students.objects.filter(student_group=current_group)
    else:
        students = Students.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET('reverse', '') == '1':
            students = students.reverse()

    context = paginate(students, 3, request, {}, var_name='students')

    return render(request, 'students/students_list.html', context)


def students_add(request):
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:

            errors = {}

            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = _("First name field is required")
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = _("Second name field if required")
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not last_name:
                errors['birthday'] = _("Birthday field is required")
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = _("It's a wrong format of date, enter correct! (For example 1984-12-30)")
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not last_name:
                errors['ticket'] = _("Ticket number is required")
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = _("Choose group for student")
            else:
                group = Groups.objects.filter(pk=student_group).first()
                if group:
                    data['student_group'] = group
                else:
                    errors['student_group'] = "Оберіть коректну групу"

            photo = request.POST.get('photo')
            if photo:
                data['photo'] = photo

            if not errors:
                student = Students(**data)
                student.save()

                return HttpResponseRedirect(f'{reverse("home")}?status_message={_("Student added successfully")}')
            else:
                return render(request, 'students/add_student.html',
                              {'groups': Groups.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(f'{reverse("home")}?status_message={_("Adding of students is canceled")}')
    else:
        return render(request, 'students/add_student.html',
                      {'groups': Groups.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Students Edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
