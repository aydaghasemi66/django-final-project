from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, ReplyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count



def blog(request, cat=None, writer=None, tag=None):
    # Rename the queryset of tags to avoid conflict
    all_tags = Tags.objects.all()
    
    # Initialize the blog queryset with all blog posts
    blog_queryset = Blog.objects.all()
    
    if cat:
        # Filter by category name
        blog_queryset = blog_queryset.filter(category__name=cat)
    elif tag:
        # Filter by tags name using the 'tags' variable
        blog_queryset = blog_queryset.filter(tag__name=tag)
    elif writer:
        # Filter by writer username
        blog_queryset = blog_queryset.filter(writer__info__username=writer)
    elif request.GET.get('search'):
        # Filter by search query
        search_query = request.GET.get('search')
        blog_queryset = blog_queryset.filter(content__contains=search_query)
    else:
        # Filter for active blog posts
        blog_queryset = blog_queryset.filter(status=True)
    
    # Annotate categories with the count of active blog posts in each category
    categories = Category.objects.annotate(blog_count=Count('blog', filter=Q(blog__status=True)))

    # Create a Paginator object for the filtered blog posts
    paginator = Paginator(blog_queryset, 6)  # 6 blog posts per page
    page_number = request.GET.get('page')
    
    try:
        # Try to get the requested page
        page = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If the page number is not an integer, get the first page
        page = paginator.page(1)
    except EmptyPage:
        # If the page number is out of range, get the last page
        page = paginator.page(paginator.num_pages)

    category = Category.objects.all()

    context = {
        "blogs": page,
        'first_page': 1,
        'last_page': paginator.num_pages,
        "categories": categories,
        'category': category,
        'tags': all_tags,  # Include all tags in the context
    }

    return render(request, 'blogs/blog.html', context=context)

@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    cid = comment.which_blog.id
    comment.delete()
    return redirect (f'/blog/blog-detail/{cid}')

@login_required
def edit(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        

        context = {
            'comment' : comment,
        }
        return render(request,'blogs/edit.html',context=context)
    
    elif request.method == 'POST' :
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            cid = comment.which_blog.id
            return redirect (f'/blog/blog-detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'Invalid data')
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
        return render(request,'blogs/reply.html',context=context)
    
    elif request.method == 'POST' :
        form = ReplyForm(request.POST)
        if form.is_valid():
            request.user.username = request.user
            form.save()
            cid = comment.which_blog.id
            return redirect (f'/blog/blog-detail/{cid}')

        else:
            messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
            return redirect (request.path_info)

def blog_detail(request, id, tag=None):
    if request.method == 'GET':
        try:
            blog = Blog.objects.get(id=id)
            comments = Comment.objects.filter(which_blog=id, status=True)
            reply = Reply.objects.filter(status=True)
            
            # Retrieve the list of all blog IDs
            blogs = Blog.objects.filter(status=True)
            id_list = [cr.id for cr in blogs]

            # Check if id_list is empty or contains only one item
            if not id_list:
                next_blog = previous_blog = None
            elif len(id_list) == 1:
                next_blog = previous_blog = None
            else:
                # Calculate the index of the current blog ID in id_list
                current_index = id_list.index(id)
                
                # Handle edge cases for the first and last elements
                if current_index == 0:
                    next_blog = Blog.objects.get(id=id_list[1])
                    previous_blog = None
                elif current_index == len(id_list) - 1:
                    next_blog = None
                    previous_blog = Blog.objects.get(id=id_list[current_index - 1])
                else:
                    next_blog = Blog.objects.get(id=id_list[current_index + 1])
                    previous_blog = Blog.objects.get(id=id_list[current_index - 1])

            # Retrieve the category queryset
            categories = Category.objects.annotate(blog_count=Count('blog', filter=Q(blog__status=True)))

            # Retrieve the tags queryset
            tags = Tags.objects.all()

            context = {
                "blog": blog,
                'next_blog': next_blog,
                'previous_blog': previous_blog,
                'comments': comments,
                'reply': reply,
                'categories': categories,
                'tags': tags,  # Include the tags queryset in the context
            }
            return render(request, 'blogs/blog-details.html', context=context)
        
        except Blog.DoesNotExist:
            return render(request, 'blogs/404.html')

    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            request.user.username = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment submitted ')
            return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, 'your comment data is not valid')
            return redirect(request.path_info)




   