from django_filters import rest_framework as filters
from Products.models import ProductImage,Products
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name = "ProductName__category__CategoryName", lookup_expr = 'in')
    price = filters.RangeFilter(field_name = "ProductName__price")

    class Meta:
        model = ProductImage
        fields = ['category','price']