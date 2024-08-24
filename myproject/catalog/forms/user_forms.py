from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from catalog.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'avatar', 'phone_number', 'country')
        labels = {
            'email': 'Электронная почта',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'avatar': 'Аватар',
            'phone_number': 'Номер телефона',
            'country': 'Страна',
        }


class CustomAuthenticationForm(AuthenticationForm):
    """
    Форма для авторизации пользователя.
    """
    username = forms.EmailField(label='Электронная почта')


class PasswordResetRequestForm(forms.Form):
    """
    Форма для запроса восстановления пароля.
    """
    email = forms.EmailField(label="Электронная почта", max_length=254)
