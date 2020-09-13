from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
from django.urls import reverse



class BlogTags(models.Model):
  tag_name = models.CharField(max_length=20)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True,auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False,auto_now=True)

  class Meta:
    verbose_name = "Теги"
    verbose_name_plural = "Тег"

  def __str__(self):
    return '%s %s' % (self.id, self.tag_name)
    


class Blog(models.Model):
  blog_title = models.CharField(max_length=250)
  blog_content = models.TextField()
  blog_img = models.ImageField(upload_to='imagesDB')
  blog_admin = models.ForeignKey(User,null = True,on_delete= models.CASCADE)
  blog_tags = models.ManyToManyField(BlogTags)
  is_active = models.BooleanField(default=True)
  url = models.SlugField(max_length = 130,unique = True)
  created_time = models.DateTimeField(auto_now_add=True,auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False,auto_now=True)

  class Meta:
    verbose_name = "Блог"
    verbose_name_plural = "Блог"
    ordering = ["-created_time"]

  def __str__(self):
    return '%s' % (self.blog_title)

  def get_absolute_url(self):
    return reverse("blog_detail",kwargs={"slug":self.url})

  def get_review(self):
    return self.commentblog_set.filter(parent__isnull = True)



  
class CommentBlog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,on_delete= models.CASCADE)
    article = models.ForeignKey(Blog,on_delete = models.CASCADE,null=True)
    comment_text = models.TextField()
    parent = models.ForeignKey('self',verbose_name = "Родитель",on_delete = models.CASCADE,blank = True,null =True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name='Комментария статьти'
        verbose_name_plural = 'Комментарии статьти'

    def __str__(self):
        return '%s %s' % (self.id, self.user)


