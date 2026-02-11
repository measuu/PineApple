from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import CartItem, Cart


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    item = cart.items.filter(product=product).first()
    if item:
        item.quantity += 1
        item.save()
    else:
        item = CartItem.objects.create(product=product)
        cart.items.add(item)

    return redirect('product_detail', product.id)

@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum([item.product.price * item.quantity for item in items])

    context = {
        'cart': {
            'items': items
        },
        'total': total
    }
    return render(request, 'cart/checkout.html', context)


def remove_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(CartItem, id=item_id)
        item.delete()
    return redirect('checkout_page')