from django.shortcuts import render, get_object_or_404
from .models import *

def portfolio_detail(request, id):
    try:
        portfolio = Portfolio.objects.get(id=id)
       

        context ={"portfolio": portfolio,
            }
        return render(request,'portfolio/portfolio-details.html',context=context)
    except:
        return render(request,'portfolio/404.html')
    
# Create your views here.
def portfolio(request, cat=None):
    category=Category.objects.all()
   
    images=PortfolioImage.objects.all()
    if cat:
        portfolio = Portfolio.objects.filter(category__name=cat)

    else:
        portfolio=Portfolio.objects.all()
    context={
        'cat': category,
        'portfolio':portfolio,
        'images':images
    }
    return render(request,"portfolio/portfolio.html",context=context)


     