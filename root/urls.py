from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path("",home,name="home"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path('service', service, name='service'),
    path('portfolio',portfolio , name='portfolio'),
    path('team',team , name='team'),
    path('blog',blog , name='blog'),

]