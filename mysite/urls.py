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
from Products.views import ContactPageView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
# from mainApp.views import login

urlpatterns = [
    re_path(r'^$',views.index, name="index"),
    path('admin/', admin.site.urls),
    path('products/', include("Products.urls")),
    path('blog/', include("Blog.urls")),
    path('accounts/',include("Profile.urls")),
    path('administration/',include("Administrations.urls")),
    path('basket/',include("Basket.urls")),
    path('order/',include("Order.urls")),

    path('api/v1/',include("API.urls")),
    path('api-auth/',include("rest_framework.urls")),

    path('auth/',include("djoser.urls")),
    path('auth/',include("djoser.urls.authtoken")),
    path('auth/',include("djoser.urls.jwt")),

    path('contact/',ContactPageView.as_view(),name="contact"),
    path('about/',views.about,name = "about_store"),
    path('check-username/',views.check_username,name = "check_username"), 

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), 

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)