from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contact, name='contact'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
