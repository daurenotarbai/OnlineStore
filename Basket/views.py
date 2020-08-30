from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect,HttpResponseNotFound, JsonResponse
from django.views.generic import TemplateView
from Products.models import Category,ProductImage,Products, Size_products,Color_products

from Basket.models import ProductsInBasket,ProductsInWishlist
from Order.models import Order,ProductsInOrder
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect,csrf_exempt
# from Products.forms import BasketCheckoutForm
from django.contrib.auth import authenticate,get_user_model,login,logout
from Products.forms import UserLoginForm, UserRegisterForm
from django.shortcuts import get_list_or_404,get_object_or_404 

@login_required
def basket_adding(request):
  return_dict = dict()
  # session_key = request.session.session_key
  user = request.user
  print (request.POST)
  data = request.POST
  nmb = data.get("nmb")
  product_id = data.get("product_id")
  price = data.get("price")
  name = data.get("name")
  product_size = data.get("product_size")
  product_color = data.get("product_color")

  is_delete = data.get("is_delete")
  if is_delete == 'true':
    ProductsInBasket.objects.filter(id = product_id).delete()
    #update(is_active = False)
  else:

    pr_in_basket, created = ProductsInBasket.objects.get_or_create(user=user,product_id = product_id,size_pr=product_size,color_pr=product_color, defaults ={"nmb" : nmb})
    if not created:
        print("not created")
        pr_in_basket.nmb+= float(nmb)
        pr_in_basket.save(force_update = True)
#common code for 2 cases
  products_in_minibasket = ProductsInBasket.objects.filter(user=user,is_active = True)
  products_total_nmb = products_in_minibasket.count()

  return_dict["products_total_nmb"] = products_total_nmb

  return_dict["products"] = list()

  for item in  products_in_minibasket:
      product_dict = dict()
      product_dict["product_id"] = item.id
      product_dict["product_name"] = item.product.ProductName.name
      product_dict["product_img"] = item.product.img.url  
      product_dict["product_price"] = item.product.ProductName.price
      product_dict["nmb"] = item.nmb
      product_dict["product_size"] = item.size_pr
      product_dict["product_color"] = item.color_pr
      product_dict["sum"] = item.nmb * item.product.ProductName.price
      return_dict["products"].append(product_dict)
  return JsonResponse(return_dict)



@login_required
def basket(request):

  # session_key = request.session.session_key
  user = request.user
  products_in_basket = ProductsInBasket.objects.filter(user=user,is_active = True)
  # form = BasketCheckoutForm(request.POST or None)
  if request.POST:
    print(request.POST)



  return render(request, "mainApp/basket.html",{"products_in_basket":products_in_basket})





@login_required
def deleting_product(request,id):
    ProductsInBasket.objects.filter(id = id).delete()
    return HttpResponseRedirect("/basket") 






@login_required
def wishlist_adding(request):
  return_dict = dict()
  # session_key = request.session.session_key
  user = request.user
  print (request.POST)
  data = request.POST
  product_id = data.get("product_id")
  print("ProductID =",product_id)
  is_delete = data.get("is_delete")
  if is_delete == 'true':
    ProductsInWishlist.objects.filter(id = product_id).delete()
    #update(is_active = False)
  else:
    pr_in_wishlist, created = ProductsInWishlist.objects.get_or_create(user=user,product_id = product_id, is_active = True)
    if not created:
        print("not created")

#common code for 2 cases
  products_in_wishlist = ProductsInWishlist.objects.filter(user=user,is_active = True)
  wishlist_total_nmb = products_in_wishlist.count()

  return_dict["wishlist_total_nmb"] = wishlist_total_nmb

  return_dict["products"] = list()

  for item in  products_in_wishlist:
      product_dict = dict()
      product_dict["product_id"] = item.id

      return_dict["products"].append(product_dict)
  return JsonResponse(return_dict)






@login_required
def wish_list(request):
  user = request.user
  products_in_wishlist = ProductsInWishlist.objects.filter(user=user,is_active = True)  

  return render(request, "mainApp/wish_list.html",{"products_in_wishlist": products_in_wishlist})