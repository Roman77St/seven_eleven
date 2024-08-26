from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Слаг', unique=True)

    class Meta:
        db_table = 'category'
        ordering = ['name',]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse("shop:product_list_category", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Слаг', unique=True)
    image = models.ImageField(upload_to='media/products', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={'slug': self.slug, 'id': self.id})
    
    class Meta:
        db_table = 'product'
        ordering = ['name',]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.name
    
