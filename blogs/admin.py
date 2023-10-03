from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Blog)
admin.site.register(Writer)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Reply)