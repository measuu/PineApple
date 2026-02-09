from django.urls import path
from . import views

urlpatterns = [
    path('catalog/<str:category>/', views.category_products, name='category_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/add_review/', views.add_review, name='add_review'),
]