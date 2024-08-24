from django.db import models


class BlogPost(models.Model):
    """
    Модель блогового поста с указанием заголовка, контента, изображений и других параметров.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    preview_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    view_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
