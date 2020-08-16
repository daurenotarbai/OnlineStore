from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from Basket.models import *
# from Profile.models import *
# from Order.models import *

class Category(models.Model):
  CategoryName = models.CharField(max_length = 20)
  CategoryImage = models.ImageField(upload_to='imagesDB')
  CategorySeason = models.CharField(max_length = 20)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
  
  @property
  def get_photo_url(self):
    if self.CategoryImage and hasattr(self.CategoryImage, 'url'):
        return self.CategoryImage.url

  def __str__(self):
      return self.CategoryName

  class Meta:
      verbose_name = 'Категория товара'
      verbose_name_plural = 'Категория товары'







class Size_products(models.Model):
  size_name = models.CharField(max_length=20, default='', null=True)
  is_active = models.BooleanField(default=True, null=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  class Meta:
      verbose_name='Размер товара'
      verbose_name_plural = 'Размер товары'
  
  def __str__(self):
    return str(self.size_name)





class Color_products(models.Model):
  color_name = models.CharField(max_length=20, default='', null=True)
  is_active = models.BooleanField(default=True, null=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  class Meta:
      verbose_name='Цвет товара'
      verbose_name_plural = 'Цвет товары'
  
  def __str__(self):
    return str(self.color_name) 





    
class Products(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 20)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True, null=True)
    elect = models.BooleanField(default= False, null = True)
    size = models.ManyToManyField(Size_products)
    color = models.ManyToManyField(Color_products)
    description = models.TextField(null = True)
    short_descrip = models.TextField(max_length=400,null=True)
    avg_rating = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    best_seller = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '%s %s' % (self.id, self.name)






class ProductImage(models.Model):
    ProductName = models.ForeignKey(Products, on_delete = models.CASCADE)
    img = models.ImageField(upload_to='imagesDB')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    # @property
    # def get_photo_url(self):
    #   if self.img and hasattr(self.img, 'url'):
    #       return self.img.url
    #   else:
    #       return "/static/images/about-01.jpg"
    class Meta:
      verbose_name = 'Изображение товара'
      verbose_name_plural = 'Изображение товаров'
    class Meta:
        ordering =['-created_time']

    def __int__(self):
      return self.id    


class RatingProduct(models.Model):
    ip =  models.CharField("IP адрес", max_length=15)
    star = models.SmallIntegerField("Значение",default = 0)
    product = models.ForeignKey(ProductImage,on_delete=models.CASCADE,blank = True,related_name = 'ratings')

    class Meta:
        verbose_name='Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return '%s' % (self.star)

class CommentProduct(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,on_delete= models.CASCADE)
    product = models.ForeignKey(Products,on_delete = models.CASCADE,related_name = "comments")
    parent = models.ForeignKey('self',verbose_name="Родитель",on_delete = models.SET_NULL,blank =True,null = True,related_name = "children")
    comment_text = models.TextField()
    rating = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


    class Meta:
        verbose_name='Комментария товара'
        verbose_name_plural = 'Комментарии товары'

    def __str__(self):
        return '%s %s' % (self.id, self.user)





def rating_for_product_post_save(sender, instance, created, **kwargs):
    product = instance.product
    all_comments_in_product = CommentProduct.objects.filter(product=product)
    all_comments_in_product_number = all_comments_in_product.count()
    total_rating = 0
    for item in all_comments_in_product:
        total_rating += item.rating

    rating_avg = total_rating / all_comments_in_product_number
    instance.product.avg_rating = rating_avg
    instance.product.save(force_update=True)


post_save.connect(rating_for_product_post_save, sender=CommentProduct)