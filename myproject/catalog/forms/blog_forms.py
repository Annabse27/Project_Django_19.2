from django import forms
from catalog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    """
    Форма для создания и редактирования блоговых постов.
    """
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'preview_image', 'is_published']
