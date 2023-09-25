from django.db import models

# Create your models here.
class Writer(models.Model):
    #info = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='writer', default='writer.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Blog(models.Model):
    writerimage = models.ImageField(upload_to='writerimage',default='default.jpg')
    contentimage = models.ImageField(upload_to='contentimage',default='default.jpg')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    quote = models.TextField()
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE)
    counted_comment = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.content[:20] + '...'
    
    def capt(self):
        return self.title.capitalize()
    

    