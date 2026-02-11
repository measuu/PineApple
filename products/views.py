from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .filters import ProductFilter


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

def category_view(request, category):
    products = Product.objects.filter(category=category)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_rating = request.GET.get('min_rating')
    max_rating = request.GET.get('max_rating')

    if min_price:
        try:
            min_price_val = float(min_price)
            products = products.filter(price__gte=min_price_val)
        except ValueError:
            pass

    if max_price:
        try:
            max_price_val = float(max_price)
            products = products.filter(price__lte=max_price_val)
        except ValueError:
            pass

    if min_rating or max_rating:
        filtered_products = []
        for product in products:
            avg_rating = product.average_rating()
            if min_rating:
                try:
                    if avg_rating < int(min_rating):
                        continue
                except ValueError:
                    pass
            if max_rating:
                try:
                    if avg_rating > int(max_rating):
                        continue
                except ValueError:
                    pass
            filtered_products.append(product)
        products = filtered_products

    context = {
        'category': category,
        'products': products,
        'request': request
    }

    return render(request, 'catalog/category.html', context)