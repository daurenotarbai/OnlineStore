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
from API import views

# from mainApp.views import login

urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('category/<int:pk>', views.CategoryView.as_view()),

    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>', views.ProductDetailView.as_view()),
    path('products/new-arrivals', views.ProductListNewArrivalsView.as_view()),
    path('products/best-seller/', views.ProductListBestSellerView.as_view()),

    path('comment/', views.ProductCommentCreatetView.as_view()),
    path('comment/<int:pk>', views.ProductCommentDestroyView.as_view()),

    path('rating/', views.AddStarProductRatingView.as_view()),

    path('administration/oreders', views.OrderListView.as_view()),








    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)