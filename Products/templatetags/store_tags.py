from django import template
from Products.models import Category, ProductImage

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.filter(is_active = True)


@register.inclusion_tag('tags/products_may_like.html')
def get_may_like_products(count = 3):
    products_may_like = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-created_time")[:count]
    return {"products_may_like":products_may_like}
