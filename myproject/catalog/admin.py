from .models import Category, Product, BlogPost, Version
from users.models import CustomUser
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Настройка отображения модели Category в административной панели Django.
    """
    list_display = ('id', 'name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Настройка отображения модели Product в административной панели Django.
    """
    list_display = ('id', 'name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

class BlogPostAdmin(admin.ModelAdmin):
    """
    Настройка отображения модели BlogPost в административной панели Django.
    """
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Version)  # для регистрации модели Version



class CustomUserAdmin(UserAdmin):
    """
    Настройка отображения и управления моделью CustomUser в административной панели Django.
    """
    model = CustomUser
    list_display = ('email', 'phone_number', 'country', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'phone_number')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('avatar', 'phone_number', 'country')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'avatar', 'phone_number', 'country'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)



