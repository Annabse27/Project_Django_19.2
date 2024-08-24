from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm
from catalog.models import Product
from django.urls import reverse_lazy


class ProductListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка продуктов.
    """
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        for product in products:
            current_version = product.versions.filter(is_current=True).first()
            if current_version:
                product.current_version = current_version
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения деталей продукта.
    """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания нового продукта.
    """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для обновления существующего продукта.
    """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'


    def get_success_url(self):
        return reverse('product_detail', args=[self.object.pk])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления продукта.
    """
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('index')
