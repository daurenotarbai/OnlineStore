from django.contrib.auth.models import User
from Products.models import Products
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from Products.models import *
# from Profile.models import *
# from Basket.models import *

class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete= models.CASCADE)
    total_price = models.FloatField(default=0)#total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_country = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_state = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_poscode = models.IntegerField(default=0)
    customer_coupone = models.CharField(default="No",max_length=12)
    comment = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.user.username)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'







class ProductsInOrder(models.Model):
  order = models.ForeignKey(Order, blank=True, null=True,on_delete= models.CASCADE)
  product = models.ForeignKey(ProductImage,on_delete= models.CASCADE,null = True)
  is_active = models.BooleanField(default=True, null=True)
  size = models.ManyToManyField(Size_products, )
  color = models.ManyToManyField(Color_products, )
  nmb =models.IntegerField(default=1,null =True)
  price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  total_price = models.DecimalField(null=True, default = 1,decimal_places=2,max_digits=10)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  class Meta:
      verbose_name = 'Товар в заказе'
      verbose_name_plural = 'Товары в заказе'

  def __str__(self):
      return "Товар %s %s" % (self.id, self.product.ProductName.name)  


  
  def save(self, *args, **kwargs):
      price_per_item = self.product.ProductName.price
      self.price_per_item = price_per_item
      print (self.nmb)

      self.total_price = int(self.nmb) * price_per_item

      super(ProductsInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductsInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductsInOrder)
