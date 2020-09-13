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

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Blog import views

# from mainApp.views import login

urlpatterns = [

    path('',views.ArticleListView.as_view(),name = "blog"),
    path('search/',views.search_article,name = "search_article"),
    path('<slug:slug>/',views.BlogDetailView.as_view(),name = "blog_detail"),
    path('add-comment/', views.adding_blog_comment,name="adding_blog_comment"),
    path('delete-comment/<int:id>', views.deleting_blog_comment,name="deleting_blog_comment"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)