from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('demo.urls')),
    url(r'^regist/', include('regist.urls')),
    url(r'^admin/', include(admin.site.urls)),
                       )