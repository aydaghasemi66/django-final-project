from django.urls import path
from .views import *


app_name = 'blogs'

urlpatterns = [
    path("", blog,name='blog'),
    path("category/<str:cat>",blog,name="blog_cat"),
    path("writer/<str:writer>",blog,name="blog_writer"),
    path("search/",blog,name="blog_search"),
    path("blog-detail/<int:id>",blog_detail,name="blog_detail"),
    path("<int:id>",delete_comment,name="delete"),
    path("edit/comment/<int:id>",edit,name="edit"),
    path("comment/reply/<int:id>",reply,name="reply"),
    path("tags/<str:tag>",blog,name="blog_tag"),
]

