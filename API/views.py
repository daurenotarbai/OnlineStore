from django.shortcuts import render

from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_list_or_404,get_object_or_404 
from rest_framework.response import Response
from rest_framework.views import APIView
from Products.models import Category
from .serializers import *
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from Basket.models import *
from django_filters.rest_framework import DjangoFilterBackend
from API.service import *

class CategoryView(APIView):
    #asasasa
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True,context={"request":request})
        return Response({"data":serializer.data})
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = CategoryPostSerializer(data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)  
        else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put (self,request,pk):
        category = Category.objects.get(pk=pk)
        serializer = CategoryUpdateSerializer(category, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self,request,pk,format=None):
        serializer = Category.objects.get(pk=pk)
        serializer.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)




class ProductListView(APIView):
 
    def get(self, request):
        products = ProductImage.objects.filter(is_active = True).annotate(
            rating_user = models.Count("ratings",filter = models.Q(ratings__ip = get_client_ip(request)))
            ).annotate(avr_star = models.Sum(models.F('ratings__star'))/models.Count(models.F('ratings'))
            )
        serializer = ProductListSerializer(products,many = True)
        return Response({"data":serializer.data})


class ProductListNewArrivalsView(APIView):
    def get(self, request):
        products = ProductImage.objects.filter(is_active = True).order_by("-created_time").annotate(
            rating_user = models.Count("ratings",filter = models.Q(ratings__ip = get_client_ip(request)))
            ).annotate(avr_star = models.Sum(models.F('ratings__star'))/models.Count(models.F('ratings'))
            )
        serializer = ProductListSerializer(products,many = True)
        return Response({"data":serializer.data})

class ProductListBestSellerView(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class  = ProductFilter
    serializer_class = ProductListSerializer
    def get_queryset(self):
        products = ProductImage.objects.filter(is_active = True).order_by("-ProductName__best_seller").annotate(
            rating_user = models.Count("ratings",filter = models.Q(ratings__ip = get_client_ip(self.request)))
        ).annotate(
            avr_star = models.Sum(models.F('ratings__star'))/models.Count(models.F('ratings'))
        )
        return products
        

class ProductDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request,pk):
        products = Products.objects.filter(is_active =True,pk=pk)
        serializer = ProductDetailSerializer(products, many = True)
        return Response({"data":serializer.data}) 

class ProductCommentCreatetView(generics.CreateAPIView):

    serializer_class = ProductCommentCreateSerializer
    queryset = CommentProduct.objects.all()

class ProductCommentDestroyView(generics.DestroyAPIView):

    queryset = CommentProduct.objects.all()

class AddStarProductRatingView(generics.CreateAPIView):
    serializer_class = RatingProductCreateSerializer
    queryset = RatingProduct

    def perform_create(self, serializer):
        serializer.save(ip = get_client_ip(self.request))


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

class OrderListView(APIView):

    def get(self,request):
        order = ProductsInBasket.objects.filter(is_active = False)
        # product = Products.objects.filter
        serializer = OrderListSerializer(order,many = True)
        return Response({"data":serializer.data}) 
