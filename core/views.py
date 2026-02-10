from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def home_view(request):
    query = request.GET.get("q", "").strip()

    products = Product.objects.filter(name__icontains=query) if query else None
    if products and products.count() == 1:
        product = products.first()
        return redirect('product_detail', product.id)

    return render(request, "core/home.html", {"products": products})