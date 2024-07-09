from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    return render(request, 'catalog/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Спасибо за ваше сообщение!")
    else:
        form = ContactForm()
    return render(request, 'catalog/contact.html', {'form': form})
