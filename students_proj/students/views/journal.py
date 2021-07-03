from django.http import HttpResponse
from django.shortcuts import render


def journal(request):
    return HttpResponse('<h1>This is Journal</h1>')
