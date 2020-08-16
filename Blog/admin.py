from django.contrib import admin
from Blog.models import Blog, BlogTags, CommentBlog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields]

    
admin.site.register(Blog,BlogAdmin)


class BlogTagsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BlogTags._meta.fields]

admin.site.register(BlogTags,BlogTagsAdmin)

class CommentBlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CommentBlog._meta.fields]

    
admin.site.register(CommentBlog,CommentBlogAdmin)