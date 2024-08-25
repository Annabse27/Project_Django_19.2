from django.urls import path
from catalog.views.product_views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
)
from catalog.views.blog_views import (
    BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
)
from catalog.views.user_views import SignupView, CustomLoginView, CustomLogoutView, EmailVerificationView, PasswordResetView
from django.views.generic import TemplateView
from catalog.views.contact_views import ContactView

from django.views.decorators.cache import cache_page
from .views.category_views import CategoryListView, ProductByCategoryListView



urlpatterns = [
    # Продукты
    path('', ProductListView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Блог
    path('blog/', BlogPostListView.as_view(), name='blogpost_list'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blog/add/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blog/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blog/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),

    # Пользователи
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('verify-email/<int:user_id>/', EmailVerificationView.as_view(), name='email_verification'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),

    # Контактная форма
    path('contacts/', ContactView.as_view(), name='contact'),

    # Лэндинг
    path('welcome/', TemplateView.as_view(template_name='catalog/landing.html'), name='landing'),

    #Кеширование
    path('product/<int:pk>/', cache_page(60 * 15)(ProductDetailView.as_view()), name='product_detail'),

    #Другие пути...
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', ProductByCategoryListView.as_view(), name='product_by_category'),

]
