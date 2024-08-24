from django import forms
from catalog.models import Product
import re


# Список запрещенных слов
PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    """
    Форма для создания и редактирования продукта.
    """
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



