from django.shortcuts import render, get_object_or_404
from .models import Product


def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_products.html', {
        'products': products,
        'category': category
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {
        'product': product
    })