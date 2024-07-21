from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ContactForm, ProductForm
from django.core.paginator import Paginator

def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)  # Показывать 4 продукта на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
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

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
