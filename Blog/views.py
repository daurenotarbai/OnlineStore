from django.shortcuts import render,redirect
from Blog.models import Blog, BlogTags,CommentBlog
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from Products.models import ProductImage
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import AddBlogCommentForm
# Create your views here.

class BlogDetailView(DetailView):
  model = Blog
  template_name = "blog/blog_detail.html"
  context_object_name = "blog_contents"
  slug_field = "url"
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['blog_tags'] = BlogTags.objects.all()
    return context


class ArticleListView(ListView):
  template_name = "blog/blog.html"
  context_object_name = "articles"
  paginate_by = 2
  queryset = Blog.objects.filter(is_active = True)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['blog_tags'] = BlogTags.objects.all()
    return context



def search_article(request):
  context = {}
  if request.method == 'GET':
    query = request.GET.get('search-article')
    if query:
      blog_contents = Blog.objects.filter(Q(blog_title__icontains = query)|Q(blog_tags__tag_name__icontains = query)|Q(blog_content__icontains = query),is_active = True)
      blog_contents_number = blog_contents.count()
      products_may_like = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-created_time")[:3]
      
      paginator = Paginator(blog_contents,2)
      page_number = request.GET.get('page',1)
      page = paginator.get_page(page_number)
      is_paginated = page.has_other_pages()
      context['articles'] = page
      context['query'] = query
      context['blog_contents_number'] = blog_contents_number
      context['is_paginated'] = is_paginated
      context['products_may_like'] = products_may_like
      

  
  return render(request, "blog/search_article.html",context = context)

def adding_blog_comment(request):

  print ("on process")
  return_dict = dict()
  # session_key = request.session.session_key
  user = request.user
  print (request.POST)
  comment_text = request.POST.get("comment_text")
  blog_id = request.POST.get("blog_id")
  comment_id = request.POST.get("comment_id")
   

  form = AddBlogCommentForm(request.POST)
  blog = Blog.objects.get(id = blog_id)

  if form.is_valid():
    form = form.save(commit = False)
    if request.POST.get("parent", None):
      form.parent_id = int(request.POST.get("parent"))
    form.user = user
    form.article = blog
    form.save()
 

  comment_blog = CommentBlog.objects.filter(article__id = blog_id, comment_text = comment_text,user = user)

  return_dict["comments"] = list()

  for item in comment_blog:
      comment_dict = dict()
      comment_dict["comment_id"] = item.id
      comment_dict["blog_id"] = item.article.id
      comment_dict["comment_text"] = item.comment_text
      comment_dict["username"] = item.user.username  
      return_dict["comments"].append(comment_dict)
  return JsonResponse(return_dict)



def deleting_blog_comment(request,id):
  url = request.META.get('HTTP_REFERER')
  user = request.user

  if request.method == "POST":
    co = CommentBlog.objects.filter(id = id)
    co.delete()
    
    messages.success(request, 'Comment is deleted successfully!!!')
  else:
    messages.error(request,"You can't delete this comment. Because this comment is not yours")

  return HttpResponseRedirect(url)