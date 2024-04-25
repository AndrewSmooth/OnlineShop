from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    rating = models.DecimalField(default=0.0, max_digits=2, decimal_places=1, validators=[
            MaxValueValidator(5.0),
            MinValueValidator(0.0)], verbose_name='Рейтинг')
            

    class Meta:
        db_table = 'Товар'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('goods:product', kwargs={'product_slug': self.slug})
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        return self.price
    
    def get_rating(self):
        if self.rating:
            rating = round(self.rating * 2) / 2
            output = ['f' for i in range(int(rating))]
            if rating - int(rating) > 0:
                output.append('h')
            if 5 - rating >= 0:
                for i in range(int(5 - rating)):
                    output.append('z')
            return output