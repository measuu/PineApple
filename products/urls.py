from django.urls import path
from . import views

urlpatterns = [
    path('catalog/<str:category>/', views.category_products, name='category_products'),
]