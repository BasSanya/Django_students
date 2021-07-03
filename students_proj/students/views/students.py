from django.http import HttpResponse
from django.shortcuts import render


def students_list(request):
    students = (
        {
            'id': '1',
            'first_name': 'Дмитро',
            'last_name': 'Літвінов',
            'ticket': '235',
            'image': 'img/Dmytro.jpeg'
        },
        {
            'id': '2',
            'first_name': 'Віталій',
            'last_name': 'Подоба',
            'ticket': '440',
            'image': 'img/Vitaliy.png'
        },
        {
            'id': '1',
            'first_name': 'Андрій',
            'last_name': 'Корост',
            'ticket': '711',
            'image': 'img/Andrew.jpg'
        }
    )
    return render(request, 'students/students_list.html', {"students": students})


def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Students Edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
