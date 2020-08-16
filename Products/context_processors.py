from Basket.models import ProductsInBasket, ProductsInWishlist
from Administrations.models import RoomChat,LiveChatView
from django.db.models import Q

def getting_basket_info(request):
    user = request.user
    session_key = request.session.session_key
    if request.user.is_authenticated:

        room = RoomChat.objects.filter(Q(assistant=request.user) | Q(customer=request.user))
        messagess = LiveChatView.objects.filter(room = room[0])
        
        product_in_basket_for_total_price = ProductsInBasket.objects.filter(user=user)
        products_in_minibasket = ProductsInBasket.objects.filter(user=user,is_active = True)
        products_total_nmb = products_in_minibasket.count()
        total_price = 0
        for i in product_in_basket_for_total_price:
          total_price = total_price + i.total_price
    else:
        # product_in_basket_for_total_price = ProductsInBasket.objects.filter(session_key=session_key)
        # products_in_minibasket = ProductsInBasket.objects.filter(session_key=session_key, is_active = True)
        products_total_nmb = 0
        total_price = 0



    return locals()


def getting_wishlist_info(request):
    user = request.user
    session_key = request.session.session_key
    if request.user.is_authenticated:
        wishlist_total_nmb = ProductsInWishlist.objects.filter(user=user,is_active = True).count()

    else:

        wishlist_total_nmb = 0



    return locals()

