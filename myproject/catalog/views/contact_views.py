from django.views.generic import FormView
from catalog.forms.contact_forms import ContactForm
from django.urls import reverse_lazy

class ContactView(FormView):
    """
    Обрабатывает отображение и отправку формы обратной связи.
    """
    template_name = 'catalog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
