from django.shortcuts import render
from Blog.models import Blog, BlogTags,CommentBlog
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from Products.models import ProductImage
# Create your views here.

def blog_detail(request,id):
  user_req = request.user
  blog_contents = Blog.objects.filter(is_active = True, id = id)
  tags_for_this_articles = BlogTags.objects.filter(is_active = True,blog__id = id )
  blog_tags = BlogTags.objects.filter(is_active = True)
  products_may_like = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-created_time")[:3]
  comment = CommentBlog.objects.filter(article__id = id)
  number_comment = comment.count()
  archive = Blog.objects.filter(is_active = True)
  july = 0
  nmb = 1
  for n in archive:
    if n.created_time.month == 7:
      july +=nmb
  print("jan",july)

  return render(request,"blog/blog_detail.html",locals())
  
def blog(request):


  blog_contents = Blog.objects.filter(is_active = True)
  blog_tags = BlogTags.objects.filter(is_active = True)
  products_may_like = ProductImage.objects.filter(is_active = True, is_main = True).order_by("-created_time")[:3]
  number_comment = CommentBlog.objects.filter(is_active=True)
  paginator = Paginator(blog_contents,3)
  page_number = request.GET.get('page',1)
  page = paginator.get_page(page_number)
  is_paginated = page.has_other_pages()

  context = {}
  context['page_object']=page
  context['is_paginated']=is_paginated
  context['blog_tags']=blog_tags
  context['products_may_like']=products_may_like



            
  return render(request,"blog/blog.html", context=context)


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
    return_dict = dict()
    # session_key = request.session.session_key
    user = request.user
    print (request.POST)
    comment_req = request.POST.get("blog_review")
    blog_id = request.POST.get("blog_id")
    comment_id = request.POST.get("comment_id")
    print("blog_iD",blog_id)


    co = CommentBlog()
    co.comment_text = comment_req
    co.user = user
    blog = Blog.objects.get(id = blog_id)
    co.article = blog
    co.save()

    comment_blog = CommentBlog.objects.filter(article__id = blog_id, comment_text = comment_req,user = user)

    return_dict["comments"] = list()

    

    for item in comment_blog:
        comment_dict = dict()
        comment_dict["comment_id"] = item.id
        comment_dict["blog_id"] = item.article.id
        comment_dict["blog_review"] = item.comment_text
        comment_dict["username"] = item.user.username  
        return_dict["comments"].append(comment_dict)
    return JsonResponse(return_dict)



def deleting_blog_comment(request,id):
  url = request.META.get('HTTP_REFERER')
  user = request.user

  if request.method == "POST":
    co = CommentBlog.objects.filter(id = id,user = user)
    co.delete()
    messages.success(request, 'Comment is deleted successfully!!!')
  else:
    messages.error(request,"You can't delete this comment. Because this comment is not yours")

  return HttpResponseRedirect(url)