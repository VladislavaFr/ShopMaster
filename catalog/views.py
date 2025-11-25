from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

def index(request):
    products_list = Product.objects.order_by('-created_at')
    paginator = Paginator(products_list, 5)  # 5 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/home.html', {'page_obj': page_obj})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contact(request):
    message = ''
    if request.method == 'POST':
        message = 'Ваше сообщение отправлено!'
    return render(request, 'catalog/contacts.html', {'message': message})

def add_product(request):
    message = ''
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, pk=category_id)
        Product.objects.create(name=name, description=description, price=price, category=category)
        message = 'Товар успешно добавлен!'
    return render(request, 'catalog/add_product.html', {'categories': categories, 'message': message})
