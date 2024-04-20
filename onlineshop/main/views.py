from django.shortcuts import render
from goods.models import Product

def index(request):
    goods = Product.objects.all()

    context={
        'title': 'Onlineshop',
        'display': 'block',
        'goods': goods,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'display': 'block',
    }
    return render(request, 'main/about.html', context)

def contact(request):
    context = {
        'title': 'Контакты',
        'display': 'block',
    }
    return render(request, 'main/contact.html', context)
