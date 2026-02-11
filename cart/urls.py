from django.urls import path
from .views import add_to_cart, cart_detail, checkout, remove_item

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', cart_detail, name='cart_detail'),
    path('checkout/', checkout, name='checkout_page'),
    path('remove/<int:item_id>/', remove_item, name='cart_remove_item'),
]