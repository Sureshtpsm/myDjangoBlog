from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^artical/', include('artical.urls', namespace='artical')),
    url(r'^admin/', include(admin.site.urls)),
)
