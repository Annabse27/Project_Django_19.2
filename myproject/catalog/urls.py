from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
    ContactView, BlogPostListView, BlogPostDetailView, BlogPostCreateView,
    BlogPostUpdateView, BlogPostDeleteView, VersionCreateView, VersionUpdateView,
    VersionDeleteView, SignupView, CustomLoginView, CustomLogoutView, EmailVerificationView
)
from django.views.generic import TemplateView
from .views import test_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('blog/', BlogPostListView.as_view(), name='blogpost_list'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blog/add/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blog/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blog/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('version/add/', VersionCreateView.as_view(), name='version_create'),
    path('version/update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),
    path('version/delete/<int:pk>/', VersionDeleteView.as_view(), name='version_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('test/', test_view, name='test-view'),
    path('verify-email/<int:user_id>/', EmailVerificationView.as_view(), name='email_verification'),
    path('welcome/', TemplateView.as_view(template_name='catalog/landing.html'), name='landing'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
