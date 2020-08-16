from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect,HttpResponseNotFound, JsonResponse
from django.views.generic import TemplateView
from Products.models import Category,ProductImage,Products, Size_products,Color_products,CommentProduct
from Basket.models import ProductsInBasket, ProductsInWishlist
from Order.models import Order,ProductsInOrder
from Blog.models import Blog, BlogTags
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect,csrf_exempt

from django.contrib.auth import authenticate,get_user_model,login,logout

from django.shortcuts import get_list_or_404,get_object_or_404 

from .models import Category

from django.contrib import messages

from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    query = request.GET.get('search-product','')
    if query:
      product_img = ProductImage.objects.filter(ProductName__name = query,is_active = True, is_main = True)
      
    else:
      product_img = ProductImage.objects.filter(is_active = True, is_main = True)
      product_img_new_arrivals = product_img.order_by("-created_time")[:8]
      product_img_best_seller = ProductImage.objects.filter(is_active = True,is_main = True).order_by("-ProductName__best_seller")[:8]
      product_img_top_rate = ProductImage.objects.filter(is_active = True,is_main = True).order_by("-ProductName__avg_rating")[:8]
      categories = Category.objects.filter(is_active = True)
      articles = Blog.objects.filter(is_active = True).order_by("-created_time")


    return render(request, "mainApp/index.html",locals())





    


def search_product(request):
    product_img_number = 0
    context = {}
    if request.method == 'GET':
      query = request.GET.get('searchproduct')
      if query:
        product_img = ProductImage.objects.filter(Q(ProductName__name__icontains = query)|Q(ProductName__category__CategoryName__icontains = query)|Q(ProductName__description__icontains = query),is_active = True, is_main = True)
        product_img_number = product_img.count()
        print("number",product_img_number  )

        paginator = Paginator(product_img,4)
        page_number = request.GET.get('page',1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        context['products'] = page
        context['query'] = query
        context['product_img_number'] = product_img_number
        context['is_paginated'] = is_paginated
    
    return render(request, "mainApp/search_product.html",context = context)



def products(request):
      categories = Category.objects.filter(is_active = True)
      product_img = ProductImage.objects.filter(is_active = True, is_main = True)
      is_wishlisted = ProductsInWishlist.objects.filter(product__ProductName__id = 21)
      paginator = Paginator(product_img,8)
      page_number = request.GET.get('page',1)
      page = paginator.get_page(page_number)
      is_paginated = page.has_other_pages()
      if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
      else:
        prev_url = ''
      if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
      else:
        next_url = ''
      context = {
        
        'page_object':page,
        'categories':categories,
        'is_paginated':is_paginated,
        'prev_url':prev_url,
        'next_url':next_url,
        "is_wishlisted":is_wishlisted

      }
    
      return render(request, "mainApp/products.html",context = context)



class ContactPageView(TemplateView):
  template_name = "base/contact.html"


def about(request): 
  return render(request, "base/about.html")





def sort_by_l(request):
  if not request.user.is_authenticated:
    query = request.GET.get('search-product','')
    if query:
      product_img = ProductImage.objects.filter(Q(ProductName__name__icontains = query)|Q(ProductName__category__CategoryName__icontains = query)|Q(ProductName__description__icontains = query),is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
    else:
      product_img = ProductImage.objects.filter(is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
  else:
    query = request.GET.get('search-product','')
    if query:
      product_img = ProductImage.objects.filter(Q(ProductName__name__icontains = query)|Q(ProductName__category__CategoryName__icontains = query)|Q(ProductName__description__icontains = query),is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
    else:
      product_img = ProductImage.objects.filter(is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
  return render(request, "mainApp/products.html",locals())

def sort_by_h(request):
  if not request.user.is_authenticated:
    query = request.GET.get('search-product','')
    if query:
      product_img = ProductImage.objects.filter(Q(ProductName__name__icontains = query)|Q(ProductName__category__CategoryName__icontains = query)|Q(ProductName__description__icontains = query),is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
    else:
      product_img = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-ProductName__price")
      categories = Category.objects.filter(is_active = True)
  else:
    query = request.GET.get('search-product','')
    if query:
      product_img = ProductImage.objects.filter(Q(ProductName__name__icontains = query)|Q(ProductName__category__CategoryName__icontains = query)|Q(ProductName__description__icontains = query),is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
    else:
      product_img = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-ProductName__price")
      categories = Category.objects.filter(is_active = True)
  return render(request, "mainApp/products.html",locals())

def sort_by_date(request):
  if not request.user.is_authenticated:
    query = request.GET.get('search-product','')
    if query:
      product_img = ProductImage.objects.filter(Q(ProductName__name__icontains = query)|Q(ProductName__category__CategoryName__icontains = query)|Q(ProductName__description__icontains = query),is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
    else:
      product_img = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-ProductName__created_time")
      categories = Category.objects.filter(is_active = True)
  else:
    query = request.GET.get('search-product','')
    if query:
      product_img = ProductImage.objects.filter(Q(ProductName__name__icontains = query)|Q(ProductName__category__CategoryName__icontains = query)|Q(ProductName__description__icontains = query),is_active = True, is_main = True).order_by("ProductName__price")
      categories = Category.objects.filter(is_active = True)
    else:
      product_img = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-ProductName__created_time")
      categories = Category.objects.filter(is_active = True)
  return render(request, "mainApp/products.html",locals())






def product_detail(request, id):
  # session_key = request.session.session_key
  # if not session_key:
  #   request.session.cycle_key()
  user_req = request.user

  size_pr = Size_products.objects.filter(products__id = id)
  color_pr = Color_products.objects.filter(products__id = id)
  product_image = ProductImage.objects.filter(ProductName__id = id, is_main = True)
  product_image2 = ProductImage.objects.filter(is_active= True)
  is_wishlisted = ProductsInWishlist.objects.filter(product__ProductName__id = id)
  categories = Category.objects.all()
  comment = CommentProduct.objects.filter(product__id = id)
  comment_number = CommentProduct.objects.filter(product__id = id).count()

  return render (request, "mainApp/product_detail.html",locals())






def addProductComment(request):
  return_dict = dict()
  # session_key = request.session.session_key
  user = request.user
  print (request.POST)
  comment_req = request.POST.get("review")
  rating_req = request.POST.get("rating")
  product_id = request.POST.get("product_id")
  comment_id = request.POST.get("comment_id")
  print("product_iD",product_id)


  co = CommentProduct()
  co.comment_text = comment_req
  co.rating = rating_req
  co.user = user
  pr = Products.objects.get(id = product_id)
  co.product = pr
  co.save()

  comment_product = CommentProduct.objects.filter(product__id = product_id, comment_text = comment_req,rating = rating_req,user = user)

  return_dict["comments"] = list()

  

  for item in comment_product:
      comment_dict = dict()
      comment_dict["comment_id"] = item.id
      comment_dict["product_id"] = item.product.id
      comment_dict["review"] = item.comment_text
      comment_dict["rating"] = item.rating 
      comment_dict["username"] = item.user.username  
      return_dict["comments"].append(comment_dict)
  return JsonResponse(return_dict)





# def addProductComment(request):
#   url = request.META.get('HTTP_REFERER')
#   if request.method == "POST":
#     user = request.user
#     comment_req = request.POST.get("review")
#     rating_req = request.POST.get("rating")
#     product_id = request.POST.get("pr_id")
#     co = CommentProduct()
#     co.comment_text = comment_req
#     co.rating = rating_req
#     co.user = user
#     pr = Products.objects.get(id = product_id)
#     co.product = pr
#     co.save()
#     messages.success(request, 'Comment is added successfully!!!')
#   else:
#     messages.error(request, 'Error adding comment')

#   return HttpResponseRedirect(url)


def deleteProductComment(request,id):
  url = request.META.get('HTTP_REFERER')
  user = request.user

  if request.method == "POST":
    co = CommentProduct.objects.filter(id = id,user = user)

    co.delete()
    messages.success(request, 'Comment is deleted successfully!!!')
  else:
    messages.error(request,"You can't delete this comment. Because this comment is not yours")

  return HttpResponseRedirect(url)






    





@login_required
def addProduct(request):
  product = Products.objects.all()
  category = Category.objects.filter(is_active = True)
  size_pr = Size_products.objects.filter(is_active = True)
  color_pr = Color_products.objects.filter(is_active = True)
  image = ProductImage.objects.filter(is_active = True)
  return render (request, "adminka/add_product.html",{"product": product,"category":category,"image":image,"size_pr":size_pr,"color_pr":color_pr})

@login_required
def addSize(request):

  user = request.user
  return render (request, "adminka/add_size.html",{"user":user})


@login_required
def addColor(request):
  
  user = request.user
  return render (request, "adminka/add_color.html",{"user":user})


@login_required
def addCategory(request):
  user = request.user
  return render (request, "adminka/add_category.html",{"user":user})

@login_required
def addArticle(request):
  article_tag = BlogTags.objects.filter(is_active = True)
  user = request.user
  return render (request, "adminka/add_article.html",{"user":user,'article_tag':article_tag})

@login_required
def addArticleTag(request):
  user = request.user
  return render (request, "adminka/add_article_tag.html",{"user":user})


@login_required
def createProduct(request):
    if request.method == "POST":

        mid = request.POST.get("product_category")
        mid2 = request.POST.get("product_name")
        mid3 = request.POST.get("product_price")
        mid4 = request.POST.get("product_size")
        mid5 = request.POST.get("product_color")
        mid6 = request.POST.get("product_description")
        mid7 = request.POST.get("product_short_description")
        mid8 = request.POST.get("product_material")
        mid9 = request.POST.get("product_weight")
        image = ProductImage()
        image.img = request.FILES["product_img"]
        category = Category.objects.get(CategoryName = mid)
        size = Size_products.objects.filter(size_name = mid4)
        color = Color_products.objects.filter(color_name = mid5)
        instance = Products.objects.create(name = mid2,price = mid3,category=category,description = mid6,
                                          short_descrip = mid7)
        instance.size.set(size)
        instance.color.set(color)

        image.ProductName = instance
        image.is_main = True
    
        image.save()

        messages.success(request, 'Product is added successfully!!!')
    else:
        messages.error(request, 'Error adding new product')

    return HttpResponseRedirect("/products/add/product/")

@login_required
def createCategory(request):
    if request.method == "POST":
      mid1 = request.POST.get("category_name")
      mid2 = request.POST.get("category_season")
      mid3 = request.FILES["category_img"]
      category = Category(CategoryName = mid1,CategorySeason = mid2, CategoryImage = mid3)
      category.save()
      messages.success(request, 'Category added successfully!!!')
    else:
      messages.error(request, 'Error adding new category')
    return HttpResponseRedirect("/products/add/category/")

@login_required
def createSize(request):
    if request.method == "POST":
      mid1 = request.POST.get("size_name")
      size = Size_products(size_name = mid1)
      size.save()
      messages.success(request, 'Size added successfully!!!')
    else:
      messages.error(request, 'Error adding new size')
    return HttpResponseRedirect("/products/add/size/")

def createColor(request):
    if request.method == "POST":
      mid1 = request.POST.get("color_name")
      size = Color_products(color_name = mid1)
      size.save()
      messages.success(request, 'Color added successfully!!!')
    else:
      messages.error(request, 'Error adding new color')
    return HttpResponseRedirect("/products/add/color/")

@login_required
def createArticle(request):
    if request.method == "POST":
      mid1 = request.POST.get("article_title")
      mid2 = request.POST.get("article_description")
      mid3 = request.FILES["article_img"]
      mid4 = request.POST.get("article_tag")
      user = request.user
      blog_tag = BlogTags.objects.filter(tag_name = mid4)
      article = Blog.objects.create(blog_title = mid1,blog_admin=user,blog_content = mid2, blog_img = mid3)
      article.blog_tags.set(blog_tag)
      article.save()
      messages.success(request, 'Article added successfully!!!')
    else:
      messages.error(request, 'Error adding new article')
    return HttpResponseRedirect("/products/add/article/")


def createArticleTag(request):
    if request.method == "POST":
      mid1 = request.POST.get("tag_name")
      tag = BlogTags(tag_name = mid1)
      tag.save()
      messages.success(request, 'Tag added successfully!!!')
    else:
      messages.error(request, 'Error adding new tag')
    return HttpResponseRedirect("/products/add/article-tag/")

def check_username(request):
  if request.GET:
    username = request.GET["user_name"]
    
    names = {"Dauren","Dauren18","Dauren19"}
    print("username:",username)

    if username in names:
      return HttpResponse("No", content_type = 'text/html')
    else:
      return HttpResponse("Ok", content_type = 'text/html')
  else:
    return HttpResponse("No", content_type = 'text/html')
        