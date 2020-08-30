from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


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
  # comment_number = models.IntegerField(null=True,default=0)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True,auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False,auto_now=True)

  class Meta:
    verbose_name = "Блог"
    verbose_name_plural = "Блог"
    ordering = ["-created_time"]

  def __str__(self):
    return '%s %s' % (self.id, self.blog_title)



  




class CommentBlog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,on_delete= models.CASCADE)
    article = models.ForeignKey(Blog,on_delete = models.CASCADE)
    comment_text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)


    class Meta:
        verbose_name='Комментария статьти'
        verbose_name_plural = 'Комментарии статьти'

    def __str__(self):
        return '%s %s' % (self.id, self.user)

# def comment_number_post_save(sender, instance, created, **kwargs):
    # blog_contents = Blog.objects.filter(is_active=True)
    # for item in blog_contents:
      # number_comment = CommentBlog.objects.filter(article__id = item.id).count()
      # item.comment_number = number_comment
      # item.save(force_update=True)

# post_save.connect(comment_number_post_save, sender=CommentBlog)