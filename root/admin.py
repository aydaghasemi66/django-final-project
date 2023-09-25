from django.contrib import admin
from .models import Services

# Register your models here.


class AdminServices(admin.ModelAdmin):
    list_display = ['title','content','status']
    list_filter = ['status']
    search_fields = ['title']

admin.site.register(Services,AdminServices)
