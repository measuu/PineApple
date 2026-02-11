import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    min_rating = django_filters.NumberFilter(method='filter_min_rating', label='Min Rating')

    class Meta:
        model = Product
        fields = []

    def filter_min_rating(self, queryset, name, value):
        return [p for p in queryset if p.average_rating() >= value]