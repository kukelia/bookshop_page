from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('products', views.products, name = 'products'),
    path('contact', views.contact, name = 'contact'),
    path('products/<int:product_id>', views.product, name = 'product')
]