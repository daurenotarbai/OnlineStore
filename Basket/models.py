from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from Products.models import *
# from Profile.models import *
# from Order.models import *

class ProductsInBasket(models.Model):
  user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete= models.CASCADE)
  product = models.ForeignKey(ProductImage, on_delete= models.CASCADE,null = True)
  is_active = models.BooleanField(default=True, null=True)
  color_pr = models.CharField(max_length=64, blank=True, null=True, default=None)
  size_pr    = models.CharField(max_length=64, blank=True, null=True, default=None)
  nmb =models.IntegerField(default=1,null =True)
  price_per_item = models.DecimalField(null=True, default = 1,decimal_places=2,max_digits=10)
  total_price = models.DecimalField(null=True, default = 1,decimal_places=2,max_digits=10)
  session_key =models.CharField(max_length=120,blank=True, null=True, default=None)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
      return '%s %s' % (self.id, self.product.ProductName.name)

  class Meta:
    verbose_name='Товар в корзине'
    verbose_name_plural = 'Товары в корзине'
  
  def save(self, *args, **kwargs):
    price_per_item = float(self.product.ProductName.price)
    self.price_per_item = price_per_item
    self.total_price = float(self.nmb) * price_per_item

    super(ProductsInBasket, self).save(*args, **kwargs)



def best_seller_product_post_save(sender, instance, created, **kwargs):
    product = instance.product.ProductName
    total_number_of_this_product_in_order = ProductsInBasket.objects.filter(product__ProductName = product,is_active=False).count()
    instance.product.ProductName.best_seller = total_number_of_this_product_in_order
    print("total_number_of_this_product_in_order",total_number_of_this_product_in_order)
    instance.product.ProductName.save(force_update=True)
    
post_save.connect(best_seller_product_post_save, sender=ProductsInBasket)




class ProductsInWishlist(models.Model):
  user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete= models.CASCADE)
  product = models.ForeignKey(ProductImage, on_delete= models.CASCADE,null = True)
  is_active = models.BooleanField(default=True, null=True)
  session_key =models.CharField(max_length=120,blank=True, null=True, default=None)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
      return '%s %s' % (self.id, self.product)

  class Meta:
    verbose_name='Товар в wishlist'
    verbose_name_plural = 'Товары в wishlist'