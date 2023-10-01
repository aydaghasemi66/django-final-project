from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    def str(self):
        return self.name
    
class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio')

    def str(self):
        return self.image
class Portfolio(models.Model):
    image = models.ManyToManyField(PortfolioImage)
    category = models.ManyToManyField(Category)
    client = models.CharField(max_length=100)
    project_date = models.DateTimeField(default=datetime.datetime.now())
    content = models.TextField()
    title = models.TextField()
    projecturl=models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def str(self):
        return self.title
    
    def capt(self):
        return self.title.capitalize()
