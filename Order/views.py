from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from Order.models import Order,ProductsInOrder
from Basket.models import ProductsInBasket
# Create your views here.

def create_order(request):
    if request.method == "POST":

        customer_name = request.POST.get("customer_name")
        customer_phone = request.POST.get("customer_phone")
        customer_email = request.POST.get("customer_email")
        customer_country = request.POST.get("customer_country")
        customer_state = request.POST.get("customer_state")
        customer_poscode = request.POST.get("customer_postcode")
        total_price = request.POST.get("total_price")
        customer_coupone = request.POST.get("coupon_code")
        comment = request.POST.get("comment")
        user = request.user
        order = Order(user = user,total_price=total_price,customer_name=customer_name,
          customer_email=customer_email,customer_phone=customer_phone,customer_country=customer_country,
          customer_state=customer_state,customer_poscode=customer_poscode,customer_coupone=customer_coupone,
          comment=comment)
        pr_in_basket = ProductsInBasket.objects.filter(user = user)
        pr_in_basket.update(is_active = False)
        order.save()

        messages.success(request, 'Product is ordered successfully!!!')
    else:
        messages.error(request, 'Error order')

    return HttpResponseRedirect("/basket/")