from django import template
from django.utils.http import urlencode
from django.utils.safestring import mark_safe


from goods.models import Category, Product


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Category.objects.all()

@register.simple_tag(takes_context=True)
def tag_products(context):
    return Product.objects.exclude(name=context['product'].name)[:4]

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

@register.simple_tag(takes_context = True)
def get_rating_markup(context):
    product = context['product']
    rating_markup = ''
    rating_markup += '<div class="rating">'
    if product.rating:
        
        for star in product.get_rating():
             if star == 'f':
                  rating_markup += '<i class="fa fa-star"></i>'
             elif star == 'h':
                  rating_markup += '<i class="fa fa-star-half"></i>'
             elif star == 'z':
                  rating_markup += '<i class="fa fa-star-o"></i>'
        return mark_safe(rating_markup + '</div>')
    return mark_safe(rating_markup + 5*'<i class="fa fa-star-o"></i>' + '</div>')

@register.simple_tag(takes_context=True)
def get_images_count(context):
    if context['images']:
        return context['images'].count()
    return 0
        

    