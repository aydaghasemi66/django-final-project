from django.shortcuts import render




def blogs(request):
    return render(request,'blogs/blog.html')


def blog_detail(request):
    return render(request,'blogs/blog-details.html')

