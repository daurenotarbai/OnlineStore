"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from Basket import views
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

# from mainApp.views import login

urlpatterns = [
    path('basketadding/',views.basket_adding, name = "basket_adding"),
    path('',views.basket, name="basket"),
    path('delete/<int:id>',views.deleting_product,name="delete_product_basket"),
    path('wishlistadding/',views.wishlist_adding, name = "wishlist_adding"),
    path('wishlist/',views.wish_list, name="wish_list"),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)