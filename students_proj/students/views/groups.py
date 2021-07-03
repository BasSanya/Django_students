from django.http import HttpResponse
from django.shortcuts import render


def groups_list(request):
    groups = (
        {
            'id': '1',
            'name': 'МтМ-21',
            'leader': 'Дмитро Літвінов'
        },
        {
            'id': '2',
            'name': 'МтМ-22',
            'leader': 'Віталій Подоба'
        }
    )
    return render(request, 'students/groups_list.html', {"groups": groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Edit Group %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Delete Group %s</h1>' % sid)
