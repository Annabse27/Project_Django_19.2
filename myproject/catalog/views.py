import random
import string

from django.views.generic import (
    ListView, DetailView, UpdateView,
    DeleteView, FormView, View
)
from django.views.generic.edit import CreateView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password

from .forms import (
    ContactForm, ProductForm, BlogPostForm,
    VersionForm, CustomUserCreationForm,
    CustomAuthenticationForm, PasswordResetRequestForm
)
from .models import Product, BlogPost, Version, CustomUser

from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

from django.urls import reverse, reverse_lazy



# Представления для продуктов
class ProductListView(ListView):
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

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('index')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.pk])

# Представления для контактов
class ContactView(FormView):
    template_name = 'catalog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Представления для блогов
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj

class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blogpost_form.html'
    success_url = reverse_lazy('blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blogpost_form.html'

    def get_success_url(self):
        return reverse('blogpost_detail', args=[self.object.pk])

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')

# Представления для версий
class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('index')

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'

    def get_success_url(self):
        return reverse_lazy('index')

class VersionDeleteView(DeleteView):
    model = Version
    template_name = 'catalog/version_confirm_delete.html'
    success_url = reverse_lazy('index')

# Новые представления для управления пользователями
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'catalog/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправка письма с верификацией
        send_mail(
            'Подтверждение регистрации',
            'Для завершения регистрации, пожалуйста, перейдите по следующей ссылке: {}'.format(self.get_verification_link(form.instance)),
            settings.DEFAULT_FROM_EMAIL,
            [form.instance.email],
            fail_silently=False,
        )
        return response


    def get_verification_link(self, user):
        # Здесь можно реализовать генерацию ссылки для верификации почты
        return reverse_lazy('email_verification', args=[user.pk])  # пример ссылки



class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'catalog/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('landing')  # Перенаправление на страницу регистрации или выбора действия


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/signup.html', {'form': form})



def test_view(request):
    return render(request, 'catalog/test.html')



class EmailVerificationView(View):
    def get(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        if user:
            user.is_active = True
            user.save()
        return redirect('login')


class PasswordResetView(View):
    '''Контроллер для восстановления пароля'''
    def get(self, request):
        form = PasswordResetRequestForm()
        return render(request, 'catalog/password_reset_form.html', {'form': form})


    def post(self, request):
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                new_password = self.generate_random_password()
                user.password = make_password(new_password)
                user.save()
                send_mail(
                    'Восстановление пароля',
                    f'Ваш новый пароль: {new_password}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                return redirect('login')
        return render(request, 'catalog/password_reset_form.html', {'form': form, 'error': 'Пользователь с таким email не найден.'})


    def generate_random_password(self, length=8):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
