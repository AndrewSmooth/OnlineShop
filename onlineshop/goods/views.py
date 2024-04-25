from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Product

# Create your views here.

def catalog(request, category_slug=None):
    goods = Product.objects.all()

    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)

    if category_slug == "all":
        goods = Product.objects.all()
        if order_by and order_by != "default":
            goods = goods.order_by(order_by)
    else:
        products = Product.objects.filter(category__slug=category_slug)
        if order_by and order_by != "default":
            products = products.order_by(order_by)
        goods = get_list_or_404(products)


    paginator = Paginator(goods, 4)

    current_page = paginator.page(int(page))

    context = {
        'title': 'Online Shop - Каталог',
        'goods': current_page,
        'display': None,
        'slug_url': category_slug
    }

    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context)