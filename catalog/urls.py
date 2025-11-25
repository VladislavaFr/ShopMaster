from django.urls import path
from .views import index, contact, product_detail, add_product

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contact, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
]
