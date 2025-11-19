from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'catalog/home.html')

def contact(request):
    message = ''
    if request.method == 'POST':
        message = 'Ваше сообщение отправлено!'
    return render(request, 'catalog/contacts.html', {'message': message})
