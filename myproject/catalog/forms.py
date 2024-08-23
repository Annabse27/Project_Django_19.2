from django import forms
from .models import Feedback, Product, BlogPost, Version
import re

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


# Список запрещенных слов
PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']



class FormStylingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})



class ContactForm(FormStylingMixin, forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'message']



class ProductForm(FormStylingMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in PROHIBITED_WORDS:
            if re.search(r'\b' + word + r'\b', name, re.IGNORECASE):
                raise forms.ValidationError(f'Название содержит запрещенное слово: {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in PROHIBITED_WORDS:
            if re.search(r'\b' + word + r'\b', description, re.IGNORECASE):
                raise forms.ValidationError(f'Описание содержит запрещенное слово: {word}')
        return description



class BlogPostForm(FormStylingMixin, forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'preview_image', 'is_published']



class VersionForm(FormStylingMixin,forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current']


class CustomUserCreationForm(UserCreationForm):
    'Форма регистрации'
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
    'Форма авторизации'
    username = forms.EmailField(label='Электронная почта')



class PasswordResetRequestForm(forms.Form):
    """Форма для восстановления пароля"""
    email = forms.EmailField(label="Электронная почта", max_length=254)
