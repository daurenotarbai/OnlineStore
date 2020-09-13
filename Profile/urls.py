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
from Profile import views
from django.views.generic import TemplateView
from .views import login_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

# from mainApp.views import login

urlpatterns = [
    path('login/',views.login_view, name = "login_view"),
    path('register/',views.register_view,name = "register_view"),
    path('logout/',views.logout_user,name = "logout_user"),
    

 
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)