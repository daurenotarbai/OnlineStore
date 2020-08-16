from django.contrib import admin
from Profile.models import *
from Basket.models import *
from Order.models import *
from Products.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]

admin.site.register(Profile,ProfileAdmin)