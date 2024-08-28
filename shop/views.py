from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from shopping_cart.forms import CartAddProductForm

def product_list(request, slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    context = {
        'products': products,
        'category': category,
        'categories': categories,
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug)
    products = Product.objects.all().exclude(slug=slug)[:3]
    cart_product_form = CartAddProductForm()
    context = {
        'product': product, 
        'first_products': products,
        'id': id,
        'cart_product_form': CartAddProductForm,
        }
    return render(request, 'shop/product_detail.html', context)
