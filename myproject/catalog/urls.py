from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contact, name='contact'),
    path('product/add/', views.product_create, name='product_create'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]

