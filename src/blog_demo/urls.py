from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^app/v1/blogs/', include('apps.blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
