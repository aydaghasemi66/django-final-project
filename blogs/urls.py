from django.urls import path
from .views import *


app_name = 'blogs'

urlpatterns = [
    path("", blogs,name='blogs'),
    path("blog-detail/<int:id>",blog_detail,name="blog_detail"),
    path("category/<str:cat>",blogs,name="blog_cat"),
]