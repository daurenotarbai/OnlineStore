from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
  task = models.CharField(max_length=300)
  user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


  class Meta:
        verbose_name = 'Cписок дел'
        verbose_name_plural = 'Cписок дел'
        
  def __str__(self):
    return '%s' % (self.id)


class RoomChat(models.Model):
  assistant = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
  customer = models.ForeignKey(User,related_name="Клиент",on_delete = models.CASCADE)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  class Meta:
    verbose_name = "Комната чата"
    verbose_name_plural = "Комната чатов"




class LiveChatView(models.Model):
  room = models.ForeignKey(RoomChat, verbose_name = "Комната чата", on_delete= models.CASCADE)
  message = models.CharField(max_length=300,null=True)
  user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


  class Meta:
    verbose_name = "Сообщение чата"
    verbose_name_plural = "Сообщение чатов"
        
  def __str__(self):
    return '%s %s' % (self.id,self.room.id)
