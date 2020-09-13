from django  import forms
from django.contrib.auth import (
  authenticate,
  get_user_model
)
from django.contrib.auth.models import User

User = get_user_model()

from django  import forms
from .models import Category,Size_products,Color_products

class AddProductCategoryForm(forms.ModelForm):

  class Meta:
    model = Category 
    fields = ("CategoryName","CategorySeason")

class AddProductSizeForm(forms.ModelForm):

  class Meta:
    model = Size_products 
    fields = ("size_name",)

class AddProductColorForm(forms.ModelForm):

  class Meta:
    model = Color_products 
    fields = ("color_name",)




class AdminLoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
  password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
  checkbox = forms.BooleanField(widget = forms.CheckboxInput())
  def clean(self, *args, **kwargs):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

    if username and password:
      user = authenticate(username = username,password = password)
      if not user:
        raise forms.ValidationError('This user does not exist. PLease check your username and password again')
      if not user.check_password(password):
        raise forms.ValidationError('incorrect passowrd')
      if not user.is_active:
        raise forms.ValidationError('This user is not active')
    return super(AdminLoginForm,self).clean(*args, **kwargs)


class UserLoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Username"}))
  password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Password"}))

  def clean(self, *args, **kwargs):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

    if username and password:
      user = authenticate(username = username,password = password)
      if not user:
        raise forms.ValidationError('This user does not exist. PLease check your username and password again')
      if not user.check_password(password):
        raise forms.ValidationError('incorrect passowrd')
      if not user.is_active:
        raise forms.ValidationError('This user is not active')
    return super(UserLoginForm,self).clean(*args, **kwargs)





class UserRegisterForm(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Username"}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"First name"}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Last name"}))
  email = forms.EmailField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Email"}))
  phone = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Phone"}))
  password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Password"}))
  password2 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30","placeholder":"Password"}))
  class Meta:
    model =User 
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
      'phone',
      'password',
      'password2',
    ]
  def clean(self, *args, **kwargs):
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    email = self.cleaned_data.get('email')
    username = self.cleaned_data.get('username')

    if User.objects.filter(username = username).exists():
      raise forms.ValidationError('This username is already exist')

    if password != password2:
      raise forms.ValidationError('Password must match')
    if User.objects.filter(email = email).exists():
      raise forms.ValidationError('This email already being used')


    return super(UserRegisterForm,self).clean(*args, **kwargs)






# class BasketCheckoutForm(forms.Form):
  # name = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30"}))
  # phone = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30"}))
  # email = forms.CharField(widget=forms.TextInput(attrs={"class":"stext-111 cl2 plh3 size-116 p-l-62 p-r-30"}))