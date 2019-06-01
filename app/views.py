from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>project structure is ready...</h1>')
