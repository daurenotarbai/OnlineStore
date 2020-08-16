
from rest_framework import serializers
from django.contrib.auth.models import User
from Products.models import *
from API.service import *
from Basket.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ("id","username")




class CategorySerializer(serializers.ModelSerializer):

    class Meta:
      model = Category
      fields = ("id","CategoryName","CategoryImage","CategorySeason","created_time","updated_time")

class CategoryPostSerializer(serializers.ModelSerializer):
    CategoryImage = serializers.ImageField()
    class Meta:
      model = Category
      fields = ("CategoryName","CategoryImage","CategorySeason")

class CategoryUpdateSerializer(serializers.ModelSerializer):
    CategoryImage = serializers.ImageField()
    class Meta:
      model = Category
      fields = ("CategoryName","CategoryImage","CategorySeason")




class FilterProductCommentListSerializer(serializers.ListSerializer):
  #фильтр комментариев, только parent
    def to_representation(self,data):
      data = data.filter(parent = None)
      return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):

    def to_representation(self,value):
      serializer = self.parent.parent.__class__(value, context = self.context)
      return serializer.data


class ProductCommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field = "username",read_only = True)
    children = RecursiveSerializer(many = True)
    class Meta:
      list_serializer_class = FilterProductCommentListSerializer
      model = CommentProduct
      fields = ("user","comment_text","children", "rating","created_time","updated_time")

class ProductCommentCreateSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(slug_field = "username",read_only = True)
    class Meta:
      model = CommentProduct
      fields = ("user","product","parent","comment_text", "rating")



class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field = "CategoryName",read_only = True)
    comments  = ProductCommentSerializer(many = True)
    color = serializers.SlugRelatedField(slug_field = "color_name",read_only = True,many = True)
    size = serializers.SlugRelatedField(slug_field = "size_name",read_only = True,many =True)

    class Meta:
      model = Products
      fields = ("id","category", "name", "price","color","size","description","short_descrip","comments","created_time","updated_time")

class ProductListExtraSerializer(serializers.ModelSerializer):

    class Meta:
      model = Products
      fields = ("id","name", "price")

class ProductListSerializer(serializers.ModelSerializer):
    ProductName = ProductListExtraSerializer()
    rating_user = serializers.BooleanField()
    avr_star = serializers.IntegerField(default = 0)
    class Meta:
      model = ProductImage
      fields = ("ProductName","img","rating_user","avr_star")



class RatingProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
      model = RatingProduct
      fields = ("star","product")

    def create(self,validated_data):
      rating, _ = RatingProduct.objects.update_or_create(ip = validated_data.get('ip', None),product = validated_data.get('product', None),defaults = {'star':validated_data.get("star")})
      return rating




# ADMINISTRATION PAGE
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#

class OrderListSerializer(serializers.ModelSerializer):
  user = serializers.SlugRelatedField(slug_field = "username",read_only = True)
  product = serializers.CharField(read_only = True)
  class Meta:
    model = ProductsInBasket
    fields = ("product","user","total_price",)