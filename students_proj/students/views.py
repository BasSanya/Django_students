from django.http import HttpResponse
from django.shortcuts import render


def students_list(request):
    return render(request, 'students/students_list.html', {})


def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Students Edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Edit Group %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Delete Group %s</h1>' % sid)
