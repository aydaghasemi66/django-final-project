from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blogs.models import Blog

class StaticSiteMap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'root:team',
            'blogs:blog',
        ]
    
    def location(self,item):
        return reverse(item)
    
class DynamicSiteMap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Blog.objects.filter(status=True)
    
    def location(self,obj):
        return '/blog/blog_detail/%s' % obj.id