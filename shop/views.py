from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, caregory_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if caregory_slug:
        category = get_object_or_404(Category, slug=caregory_slug)
        products = products.filter(category=category)
    context = {
        'products': products,
        'category': category,
        'categories': categories,
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    products = Product.objects.all().exclude(slug=slug)[:3]
    context = {'product': product, 'first_products': products}
    return render(request, 'shop/product_detail.html', context)
