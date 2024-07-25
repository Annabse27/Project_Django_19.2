from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import BlogPost

@receiver(post_save, sender=BlogPost)
def send_congratulations_email(sender, instance, **kwargs):
    if instance.view_count == 100:
        send_mail(
            'Congratulations!',
            f'Your article "{instance.title}" has reached 100 views!',
            'annabse27@gmail.com',  # Отправитель
            ['annabse27@gmail.com'],  # Получатель
            fail_silently=False,
        )
