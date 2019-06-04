from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Quote
from .forms import QuoteForm


# def index(request):
#     return HttpResponse('<h1>project structure is ready...</h1>')

def show_all(request):
    quotes = Quote.objects.all()
    return render(request, 'app/show_all.html', {'app': quotes})


def show_one(request, pk):
    one_quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'app/show_one.html', {'quote': one_quote})


def new(request):
    form = QuoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'One quote just got added')
        return redirect('app:show_all')
    else:
        return render(request, 'app/quote_form.html', {'form': form})


def edit(request, pk):
    to_edit = get_object_or_404(Quote, pk=pk)
    form = QuoteForm(request.POST or None, instance=to_edit)

    if form.is_valid():
        form.save()
        messages.success(request, f'Updated')
        return redirect('app:show_all')
    else:
        return render(request, 'app/quote_form.html', {'form': form})


def drop(request, pk):
    to_drop = get_object_or_404(Quote, pk=pk)

    if request.method == 'POST':
        to_drop.delete()
        messages.success(request, f'{to_drop.author} quote deleted')

    return render(request, 'app/drop_confirmation.html', {'quote': to_drop})
