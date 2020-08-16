from django.contrib import admin
from Administrations.models import *
from Basket.models import *
from Order.models import *
from Products.models import *

class ToDoListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ToDoList._meta.fields]

admin.site.register(ToDoList,ToDoListAdmin)

class RoomChatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RoomChat._meta.fields]

admin.site.register(RoomChat,RoomChatAdmin)

class LiveChatViewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LiveChatView._meta.fields]

admin.site.register(LiveChatView,LiveChatViewAdmin)