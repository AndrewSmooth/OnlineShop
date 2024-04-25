from django.contrib import admin

from goods.models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'category', 'price', 'quantity', 'discount']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category', 'rating']
    fields = [
        'name',
        'slug',
        'description',
        'image',
        'price',
        'discount',
        'quantity',
        'category',
        'rating',
    ]

