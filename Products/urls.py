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
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from Products import views

# from mainApp.views import login

urlpatterns = [

    path('', views.products,name="products"),
    path('<int:id>', views.product_detail,name="product_detail"),
    path('search-product', views.search_product,name="search_product"),
    
    path('sort-by=low-to-high/', views.sort_by_l,name="sort_by_l"),
    path('sort-by=high-to-low/', views.sort_by_h,name="sort_by_h"),
    path('sort-by=newness/', views.sort_by_date,name="sort_by_date"),


    path('delete/<int:id>', views.deleteProductComment,name="delete_comment"),
    path('add-comment/', views.addProductComment,name="product_comment"),

    path('add/product/', views.addProduct,name="adding_product"),
    path('add/category/', views.addCategory, name="adding_category"),
    path('add/size/', views.addSize,name="adding_size"),
    path('add/color/', views.addColor,name="adding_color"),
    path('add/article/', views.addArticle,name="adding_article"),
    path('add/article-tag/', views.addArticleTag,name="adding_article_tag"),

    path('adding-category/',views.createCategory,name="createCategory"),
    path('adding-product/',views.createProduct,name="createProduct"),
    path('adding-size/',views.createSize,name="createSize"),
    path('adding-color/',views.createColor,name="createColor"),
    path('adding-article/',views.createArticle,name="createArticle"),
    path('adding-article_tag/',views.createArticleTag,name="createArticleTag"),




    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)