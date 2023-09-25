from django.db import models

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
