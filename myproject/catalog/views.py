from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def index(request):
    products = Product.objects.all()
    context = {'object_list': products}
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Спасибо за ваше сообщение!")
    else:
        form = ContactForm()
    return render(request, 'catalog/contact.html', {'form': form})
