from django.shortcuts import render
from django.http import HttpResponse
from django.template import context

def index(request):
    context={
        'title': 'Onlineshop',
        'display': 'block',
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
