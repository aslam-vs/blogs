from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^app/v1/blogs/', include('apps.blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
