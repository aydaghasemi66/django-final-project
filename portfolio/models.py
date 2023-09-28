from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    def str(self):
        return self.name
class Portfolio(models.Model):
    image = models.ImageField(blank=True)
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
class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='contentimage')

    def str(self):
        return self.portfolio.title