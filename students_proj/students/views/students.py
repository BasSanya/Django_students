from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ..models import Students, Groups


def students_list(request):
    students = Students.objects.all()

    # try to order student list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {"students": students})


def students_add(request):
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:

            errors = {}

            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = "Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not last_name:
                errors['birthday'] = "Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = 'Введіть коректний формат дати (наприклад 1984-12-30)'
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not last_name:
                errors['ticket'] = "Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = "Оберіть групу для студента"
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

                return HttpResponseRedirect(f'{reverse("home")}?status_message=Студент/-ка, '
                                            f'{first_name + " " + last_name}, успішно додано!')
            else:
                return render(request, 'students/add_student.html',
                              {'groups': Groups.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect('%s?status_message=Додавання студента скасовано!' % reverse('home'))
    else:
        return render(request, 'students/add_student.html',
                      {'groups': Groups.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Students Edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
