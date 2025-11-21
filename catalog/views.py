from django.shortcuts import render
from .models import Product

def index(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    print("Последние 5 продуктов:", latest_products)
    return render(request, 'catalog/home.html', {'latest_products': latest_products})

def contact(request):
    message = ''
    if request.method == 'POST':
        message = 'Ваше сообщение отправлено!'
    return render(request, 'catalog/contacts.html', {'message': message})