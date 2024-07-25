from django.urls import path
from .views import IndexView, ContactView, ProductCreateView, ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
