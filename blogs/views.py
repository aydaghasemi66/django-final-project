from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, ReplyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


def blog(request, cat=None, writer=None,tags=None):
    blog = Blog.objects.all()
    tags=Tags.objects.all()
    if cat:
        blog = blog.filter(category__name=cat)
    elif tags:
        tags=blog.filter(tag__name=tag)
    elif writer:
        blog = blog.filter(writer__info__username=writer)
    elif request.GET.get('search'):
        
        blog = blog.objects.filter(content__contains=request.GET.get('search')) 
    else:
        blog = blog.filter(status=True)
    categories = Category.objects.annotate(blog_count=Count('blog', filter=Q(blog__status=True)))

    # سپس از Paginator برای تقسیم بلاگ‌ها به صفحات استفاده می‌کنیم
    blog = Paginator(blog, 6)  # 6 بلاگ در هر صفحه
    first_page = 1
    last_page = blog.num_pages
    # می‌توانیم شماره صفحه مورد نظر را از پارامترهای درخواست دریافت کنیم
    page_number = request.GET.get('page')

    try:

       page_number = request.GET.get('page')
       blog = blog.get_page(page_number)

    except PageNotAnInteger:
        # اگر شماره صفحه معتبر نباشد، صفحه اول را بگیریم
        blog = blog.page(1)
    except EmptyPage:
        # اگر شماره صفحه بیشتر از تعداد کل صفحات باشد، صفحه آخر را بگیریم
        blog = blog.page(blog.num_pages)
    category=Category.objects.all()
    
         
 
    context ={"blogs": blog,
                  'first_page': first_page,
                  'last_page': last_page,
                  "categories": categories,
                  'category': category
    }
    return render(request, 'blogs/blog.html', context=context)


@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    cid = comment.which_blog.id
    comment.delete()
    return redirect (f'/blogs/blog-detail/{cid}')

@login_required
def edit(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        

        context = {
            'comment' : comment,
        }
        return render(request,'blog/edit.html',context=context)
    
    elif request.method == 'POST' :
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            cid = comment.which_blog.id
            return redirect (f'/blogs/blog-detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
            return redirect (request.path_info)
@login_required
def reply(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        form = ReplyForm()

        context = {
            'comment' : comment,
            'form' : form,
        }
        return render(request,'blog/reply.html',context=context)
    
    elif request.method == 'POST' :
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            cid = comment.which_blog.id
            return redirect (f'/blogs/blog-detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect (request.path_info)
def blog_detail(request, id):
    tags=Tags.objects.all()
    category=Category.objects.all()
    categories = Category.objects.annotate(blog_count=Count('blog', filter=Q(blog__status=True)))
    blog = Blog.objects.all()
    if request.method == 'GET':
        try:
            blog = Blog.objects.get(id=id)
            comments = Comment.objects.filter(which_blog=id, status=True)
            reply = Reply.objects.filter(status=True)
            id_list = []
            blogs = Blog.objects.filter(status=True)
            for cr in blogs:
                id_list.append(cr.id)   

            id_list.reverse()

            if id_list[0] == id :
                next_blog = Blog.objects.get(id = id_list[1])
                previous_blog = None  

            elif id_list[-1] == id :
                next_blog = None
                previous_blog = Blog.objects.get(id = id_list[-2])  

            else:
                next_blog = Blog.objects.get(id=id_list[id_list.index(id)+1])
                previous_blog = Blog.objects.get(id=id_list[id_list.index(id)-1])   

            blog.save()
            context ={"blog": blog,
                      'next_blog': next_blog,
                      'previous_blog': previous_blog,
                      'comments': comments,
                      'reply' : reply,
                      'category': category,
                      "categories": categories,
                      'tags':tags
            }
            return render(request,'blogs/blog-details.html',context=context)
        except:
            return render(request,'blogs/404.html')
    
    elif request.method == 'POST' and len(request.POST) > 2:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'yor comment submited and publish as soon')
            return redirect (request.path_info)
        else:
            messages.add_message(request,messages.ERROR,'yor comment data is not valid')
            return redirect (request.path_info)
        






   
