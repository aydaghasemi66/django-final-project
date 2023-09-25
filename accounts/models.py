from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.





class CustomeUser(AbstractUser):
    mobile = models.CharField(max_length=20,null=True, blank=True)
    image = models.ImageField(upload_to='users', default='user.jpg')
