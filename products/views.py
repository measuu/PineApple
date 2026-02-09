from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review


def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_products.html', {
        'products': products,
        'category': category
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    stars = range(1, 6)
    return render(request, 'products/product_detail.html', {
        'product': product,
        'stars': stars
    })

def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        rating = int(request.POST.get("rating"))
        text = request.POST.get("text")
        if rating and text:
            Review.objects.create(product=product, rating=rating, text=text)
    return redirect('product_detail', pk=product.pk)