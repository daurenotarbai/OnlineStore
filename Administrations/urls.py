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
from Administrations import views
from Administrations.views import OrderList
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

# from mainApp.views import login

urlpatterns = [
    path('admin/',views.account_view,name = "account_view"),
    path('admin/login/', views.admin_login, name="admin_login"),
    path('adding-task/', views.adding_task, name="adding_task"),
    path('deleting/task/<int:id>', views.deleting_task, name="deleting_task"),
    path('done/task/<int:id>', views.done_task, name="done_task"),
    path('send-message', views.sendMessageAssistant, name="send_message"),
    path('send-message-customer', views.sendMessageCustomer, name="send_message_customer"),
    path('orders/', OrderList.as_view(), name="order_list"),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)