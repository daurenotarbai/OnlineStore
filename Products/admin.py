from django.contrib import admin
from Profile.models import *
from Basket.models import *
from Order.models import *
from Products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage

    extra = 0




class ProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.fields]
    inlines = [ProductImageInline]

admin.site.register(Products,ProductsAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    
admin.site.register(Category,CategoryAdmin)





class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    
admin.site.register(ProductImage,ProductImageAdmin)






class Size_productsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Size_products._meta.fields]

    
admin.site.register(Size_products,Size_productsAdmin)






class Color_productsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Color_products._meta.fields]

    
admin.site.register(Color_products,Color_productsAdmin)



class CommentProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CommentProduct._meta.fields]

    
admin.site.register(CommentProduct,CommentProductAdmin)



class RatingProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RatingProduct._meta.fields]

    
admin.site.register(RatingProduct,RatingProductAdmin)