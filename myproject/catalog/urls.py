from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView,
    SignupView, CustomLoginView, CustomLogoutView, EmailVerificationView, PasswordResetView
)
from django.views.generic import TemplateView
from catalog.views.contact_views import ContactView

urlpatterns = [
    # Маршруты для продуктов (Products)
    path('', ProductListView.as_view(), name='index'),  # Главная страница с перечнем продуктов
    path('product/add/', ProductCreateView.as_view(), name='product_create'),  # Добавление продукта
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Просмотр продукта по ID
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),  # Обновление продукта по ID
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),  # Удаление продукта по ID

    # Маршруты для блогов (Blog posts)
    path('blog/', BlogPostListView.as_view(), name='blogpost_list'),  # Перечень всех блогов
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),  # Просмотр блога по ID
    path('blog/add/', BlogPostCreateView.as_view(), name='blogpost_create'),  # Добавление нового блога
    path('blog/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),  # Обновление блога по ID
    path('blog/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),  # Удаление блога по ID

    # Маршруты для управления пользователями (User management)
    path('signup/', SignupView.as_view(), name='signup'),  # Регистрация нового пользователя
    path('login/', CustomLoginView.as_view(), name='login'),  # Вход пользователя
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Выход пользователя
    path('verify-email/<int:user_id>/', EmailVerificationView.as_view(), name='email_verification'),  # Верификация email

    # Маршруты для восстановления пароля (Password reset)
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),  # Запрос на восстановление пароля

    # Маршруты для статических страниц (Static pages)
    path('contacts/', ContactView.as_view(), name='contact'),  # Страница контактов
    path('welcome/', TemplateView.as_view(template_name='catalog/landing.html'), name='landing'),  # Страница приветствия
]
