from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ContactView,
    BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView,
    VersionCreateView, VersionUpdateView, VersionDeleteView, ProductUpdateView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),  # Новый маршрут
    path('blog/', BlogPostListView.as_view(), name='blogpost_list'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blog/add/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blog/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blog/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('version/add/', VersionCreateView.as_view(), name='version_create'),
    path('version/update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),
    path('version/delete/<int:pk>/', VersionDeleteView.as_view(), name='version_delete'),
]
