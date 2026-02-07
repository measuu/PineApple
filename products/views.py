from django.shortcuts import render
from .models import Product

def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_products.html', {
        'products': products,
        'category': category
    })