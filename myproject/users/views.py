import string
import random
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from users.forms import CustomUserCreationForm, CustomAuthenticationForm, PasswordResetRequestForm
from users.models import CustomUser

from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password


class SignupView(CreateView):
    """
    Представление для регистрации нового пользователя.
    """
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            'Подтверждение регистрации',
            'Для завершения регистрации, пожалуйста, перейдите по следующей ссылке: {}'.format(self.get_verification_link(form.instance)),
            settings.DEFAULT_FROM_EMAIL,
            [form.instance.email],
            fail_silently=False,
        )
        return response


    def get_verification_link(self, user):
        return reverse_lazy('email_verification', args=[user.pk])


class CustomLoginView(LoginView):
    """
    Представление для авторизации пользователя.
    """
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    """
    Представление для выхода


 пользователя из системы.
    """
    next_page = reverse_lazy('landing')


class EmailVerificationView(View):
    """
    Представление для верификации email пользователя.
    """
    def get(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        if user:
            user.is_active = True
            user.save()
        return redirect('login')


class PasswordResetView(View):
    """
    Представление для запроса восстановления пароля.
    """
    def get(self, request):
        form = PasswordResetRequestForm()
        return render(request, 'users/password_reset_form.html', {'form': form})


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
        return render(request, 'users/password_reset_form.html', {'form': form, 'error': 'Пользователь с таким email не найден.'})


    def generate_random_password(self, length=8):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
