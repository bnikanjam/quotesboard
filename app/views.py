from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Quote
from .forms import QuoteForm


# def index(request):
#     return HttpResponse('<h1>project structure is ready...</h1>')

def show_all(request):
    quotes = Quote.objects.all()
    return render(request, 'app/show_all.html', {'quotes': quotes})


def show_one(request, pk):
    pass


def new(request):
    pass


def edit(request, pk):
    pass


def drop(request, pk):
    pass
