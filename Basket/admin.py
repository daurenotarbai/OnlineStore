from django.contrib import admin
from Profile.models import *
from Basket.models import *
from Order.models import *
from Products.models import *

class ProductsInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductsInBasket._meta.fields]

    
admin.site.register(ProductsInBasket,ProductsInBasketAdmin)



class ProductsInWishlistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductsInWishlist._meta.fields]

admin.site.register(ProductsInWishlist,ProductsInWishlistAdmin)
