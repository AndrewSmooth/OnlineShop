from django.contrib import admin

from goods.models import Category, Product, AdditionalImage, Size

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name',]

@admin.register(AdditionalImage)
class AdditionalImageAdmin(admin.ModelAdmin):
    list_display = ['product',]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'quantity']

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class SizeInline(admin.TabularInline):
    model = Size

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
    inlines = (AdditionalImageInline, SizeInline)
    


    
