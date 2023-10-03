from django.shortcuts import render , redirect
from django.contrib import messages
from .models import*
from .forms import*
from blogs.models import*

# Create your views here.



def home (request):
    category=Category.objects.all()
    services=Services.objects.filter(status=True)
    last_blog=Blog.objects.order_by('-created_date')[:5]
    context={
         'services': services,
         'category': category,
         'last_blog':last_blog,
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
    team=Team.objects.filter(status=True)
    context={
         'category': category,
         'team': team
    }
    return render(request,"root/about.html",context=context)


def contact(request):
    category=Category.objects.all()
    context={
         'category': category,
    }
    if request.method =='GET':

        return render(request,"root/contact.html",context=context)
        
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')

 
def team(request):
    category=Category.objects.all()
    team=Team.objects.filter(status=True)
    context={
         'category': category,
         'team': team
    }
    return render(request,"root/team.html",context=context)  
def blog(request):
    category=Category.objects.all()
    context={
         'category': category
    }
    return render(request,"blogs/blog.html",context=context)  


