from django.shortcuts import render , redirect
from django.contrib import messages
from .models import*
from blogs.models import*

# Create your views here.



def home (request):
    category=Category.objects.all()
    services=Services.objects.filter(status=True)
    context={
         'services': services,
         'category': category
    }
    return render(request,"root/index.html",context=context)



def service(request):
    category=Category.objects.all()
    services=Services.objects.filter(status=True)
    context={
         'services': services,
         'category': category
    }
    return render(request,"root/services.html",context=context)   

def about (request):
    category=Category.objects.all()
    context={
         'category': category
    }
    return render(request,"root/about.html")

def contact(request):
    category=Category.objects.all()
    context={
         'category': category
    }
    return render(request,"root/contact.html")

 
def portfolio(request):
    category=Category.objects.all()
    context={
         'category': category
    }
    return render(request,"root/portfolio.html")   
def team(request):
    category=Category.objects.all()
    context={
         'category': category
    }
    return render(request,"root/team.html")  
def blog(request):
    category=Category.objects.all()
    context={
         'category': category
    }
    return render(request,"blogs/blog.html")  


