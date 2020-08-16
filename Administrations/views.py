from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect,HttpResponseNotFound, JsonResponse
from django.views.generic import TemplateView,ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from Products.models import *
from Products.forms import AdminLoginForm
from Basket.models import *
from Order.models import *
from Administrations.models import *
from Profile.models import *
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator

from django.contrib.auth import authenticate,login



@login_required(login_url='/administration/admin/login')
def account_view(request):
    user = request.user
    user_number = User.objects.filter(is_staff = False,is_superuser = False).count()
    sold_products = ProductsInBasket.objects.filter(is_active = False)
    products_number = Products.objects.filter(is_active = True).count()
    orders = Order.objects.filter(is_active = True).order_by("-created_time")[:5]
    users = User.objects.all()

    tasks = ToDoList.objects.filter(user = user,is_active=True)
    done_tasks =ToDoList.objects.filter(user = user,is_active=False)

    
    room = RoomChat.objects.filter(Q(assistant=request.user) | Q(customer=request.user))

    messages = LiveChatView.objects.filter(room = room[0])


    total_amount = 0
    
    for item in sold_products:
      total_amount += item.total_price
    print("Total_amount",total_amount)
    number_of_sold_products = sold_products.count()
   
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')

    if request.user.is_superuser:
        template = 'adminka/dashboard.html'

    elif request.user.is_staff and request.user.groups.filter(name='Admin').exists():
        template = 'adminka/dashboard.html'


    elif request.user.groups.filter(name='Assistants').exists():
        template = 'adminka/assistants.html'

    else:
        template = 'adminka/error_for_clients.html'

 
    context = {
      "number_of_sold_products":number_of_sold_products,
      "total_amount":total_amount,
      "user_number":user_number,
      "products_number":products_number,
      "orders":orders,
      "users":users,
      "tasks":tasks,
      "done_tasks":done_tasks,
      "messages":messages

    }

    return render(request, template,context = context)


class OrderList(ListView):
    template_name = 'adminka/order_list.html'
    model = ProductsInOrder
    # paginate_by = 100  # if pagination is desired



    def get_context_data(self, **kwargs):
        orders = Order.objects.filter(is_active = True).order_by("-created_time")
        paginator = Paginator(orders,25)
        page_number = self.request.GET.get('page',1)
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
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['page_object'] = page
        context['prev_url'] = prev_url
        context['is_paginated'] = is_paginated
        context['next_url'] = next_url


        return context


def adding_task(request):
  url = request.META.get('HTTP_REFERER')
  user = request.user
  task = request.POST.get("adding_task")
  todolist = ToDoList(task=task,user = user)
  todolist.save()
  return HttpResponseRedirect(url)


def deleting_task(request,id):
  url = request.META.get('HTTP_REFERER')
  user = request.user
  todolist = ToDoList.objects.filter(id=id)
  todolist.delete()
  return HttpResponseRedirect(url)


def done_task(request,id):
  url = request.META.get('HTTP_REFERER')
  user = request.user
  todolist = ToDoList.objects.filter(id=id)
  todolist.update(is_active=False)
  return HttpResponseRedirect(url)



@login_required
def sendMessageAssistant(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
      user = request.user
      mid1 = request.POST.get("send_mes_livechat_from_assistant")
      room = RoomChat.objects.get(assistant=user)
      messages = LiveChatView(message = mid1,room = room,user = user)

      messages.save()

    return HttpResponseRedirect(url)

@login_required
def sendMessageCustomer(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
      user = request.user
      mid1 = request.POST.get("send_mes_livechat_from_customer")
      room = RoomChat.objects.get(customer=user)
      messages = LiveChatView(message = mid1,room = room,user = user)

      messages.save()

    return HttpResponseRedirect(url)


def admin_login(request):
  next = request.GET.get('next')
  form = AdminLoginForm(request.POST or None)
  if form.is_valid():
      
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username = username, password = password)
      login(request, user)
      if next:
        return redirect(next)
      return redirect('/')
      token = Token.objects.create(user=user)
      print(token.key)
  return render (request,"adminka/admin_login.html",{'form':form})



