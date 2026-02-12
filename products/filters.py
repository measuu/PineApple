import django_filters
from .models import Product

from django.db.models import Avg


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="gte", label="Min Price"
    )
    max_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="lte", label="Max Price"
    )
    min_rating = django_filters.NumberFilter(
        method="filter_min_rating", label="Min Rating"
    )
    max_rating = django_filters.NumberFilter(
        method="filter_max_rating", label="Max Rating"
    )

    class Meta:
        model = Product
        fields = ["min_price", "max_price", "min_rating", "max_rating"]

    def filter_min_rating(self, queryset, name, value):
        if value:
            return queryset.annotate(avg_rating=Avg("reviews__rating")).filter(
                avg_rating__gte=value
            )
        return queryset

    def filter_max_rating(self, queryset, name, value):
        if value:
            return queryset.annotate(avg_rating=Avg("reviews__rating")).filter(
                avg_rating__lte=value
            )
        return queryset
