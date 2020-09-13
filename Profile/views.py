from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect,HttpResponseNotFound, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth import login,logout,authenticate
from Products.forms import UserLoginForm,UserRegisterForm
from django.contrib import messages
from django.views.generic.edit import CreateView


# class login_view(CreateView):
#   model= User
#   form_class = UserLoginForm
#   template_name = "mainApp/login.html"
  
#   def get_success_url(self):
#     return reverse("/")



@csrf_exempt
def login_view(request):
  # session_key = request.session.session_key
  next = request.GET.get('next')
  form = UserLoginForm(request.POST or None)
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
  return render (request,"mainApp/login.html",{'form':form})



def register_view(request):
  next = request.GET.get('next')
  form = UserRegisterForm(request.POST or None)
  if form.is_valid():

      user = form.save(commit=False)
      password = form.cleaned_data.get('password')
      user.set_password(password)
      user.save()
      messages.success(request, 'You succesfully sign up our shop.</br> Please signed in the system with your personal informations')
      if next:
        return redirect(next)
      return redirect('/accounts/login')

  return render (request, "mainApp/register.html",{'form':form})




from djoser.views import TokenDestroyView

def logout_user(request):
    user = request.user
    logout(request)
    return redirect('/')