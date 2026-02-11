from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    @property
    def total(self):
        return sum(item.total_price for item in self.items.all())