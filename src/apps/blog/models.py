from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.conf import settings

import datetime
# import tagging
# from tagging.fields import TagField


class Category(models.Model):

    """Category model."""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'blog_categories'
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('blog_category_detail', None, {'slug': self.slug})


class Author(models.Model):

    """Category model."""
    name = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'), )
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        db_table = 'blog_authors'
        # ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.name


class Blog(models.Model):

    """Blog model."""
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='publish')
    author = models.ForeignKey(Author, blank=True, null=True)
    body = models.TextField(_('body'), )
    publish = models.DateTimeField(_('publish'), default=datetime.datetime.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    # tags = TagField()

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('posts')
        db_table = 'blog_posts'
        ordering = ('-publish',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('blog_detail', None, {
            'year': self.publish.year,
            'month': self.publish.strftime('%b').lower(),
            'day': self.publish.day,
            'slug': self.slug
        })


