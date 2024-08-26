from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    ordering = ['name',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    ordering = ['category', 'name']
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['category', 'available']
    list_editable = ['price', 'available']
    search_fields = ['name', 'description']



