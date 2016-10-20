from django.conf.urls import url

import apps.blog.views as views

urlpatterns = [
	url(r'^$', views.Blogs.as_view(), name='blogs'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.BlogOperation.as_view(), name='blog_operation'),

    ]