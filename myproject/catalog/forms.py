from django import forms
from .models import Feedback, Product, BlogPost

class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'preview_image', 'is_published']
