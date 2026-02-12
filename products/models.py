from django.db import models
from django.db.models import Avg


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("macbooks", "MacBooks"),
        ("iphones", "iPhones"),
        ("ipads", "iPads"),
        ("watch", "Apple Watch"),
        ("airpods", "AirPods"),
        ("accessories", "Accessories"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum(r.rating for r in reviews) / reviews.count()
        return list(range(1, 6))

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} — {self.rating}⭐"
