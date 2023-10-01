from django.urls import path
from .views import *


app_name = 'portfolio'

urlpatterns = [
    path("", portfolio,name='portfolio'),
    path("category/<str:cat>",portfolio,name="port_cat"),
    path("portfolio_detail/<int:id>",portfolio_detail,name="portfolio_detail"),
    
]

