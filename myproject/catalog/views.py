'''
1. `index` → `ListView`
2. `contact` → `FormView`
3. `product_create` → `CreateView`
4. `product_detail` → `DetailView`

'''




from django.views.generic import ListView, FormView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Product, Feedback
from .forms import ContactForm, ProductForm

class IndexView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    paginate_by = 4

class ContactView(FormView):
    template_name = 'catalog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('index')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
