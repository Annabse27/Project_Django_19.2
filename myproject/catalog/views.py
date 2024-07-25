'''
1. `index` → `ListView`
2. `contact` → `FormView`
3. `product_create` → `CreateView`
4. `product_detail` → `DetailView`

'''


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Product, BlogPost
from .forms import ContactForm, ProductForm, BlogPostForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('index')


class ContactView(FormView):
    template_name = 'catalog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blogpost_list.html'
    context_object_name = 'posts'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blogpost_detail.html'
    context_object_name = 'post'

class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blogpost_form.html'
    success_url = reverse_lazy('blogpost_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blogpost_form.html'
    success_url = reverse_lazy('blogpost_list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')

