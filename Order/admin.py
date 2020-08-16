from django.contrib import admin
from Profile.models import *
from Basket.models import *
from Order.models import *
from Products.models import *

class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductsInOrderInline]


admin.site.register(Order,OrderAdmin)


class ProductsInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductsInOrder._meta.fields]

    
admin.site.register(ProductsInOrder,ProductsInOrderAdmin)