from django.db import models
from accounts.models import CustomeUser
# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_data']

class Team(models.Model):
    info = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    fullname= models.CharField(max_length=100)
    job= models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team', default='user.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname


class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name