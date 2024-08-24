from django import forms
from catalog.models import Feedback

class ContactForm(forms.ModelForm):
    """
    Форма для обработки контактной информации пользователей.
    """
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
