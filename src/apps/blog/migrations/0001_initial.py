# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'db_table': 'blog_authors',
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug', unique_for_date=b'publish')),
                ('body', models.TextField(verbose_name='body')),
                ('publish', models.DateTimeField(default=datetime.datetime.now, verbose_name='publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('author', models.ForeignKey(blank=True, to='blog.Author', null=True)),
            ],
            options={
                'ordering': ('-publish',),
                'db_table': 'blog_posts',
                'verbose_name': 'Blog',
                'verbose_name_plural': 'posts',
                'get_latest_by': 'publish',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'ordering': ('title',),
                'db_table': 'blog_categories',
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', blank=True),
            preserve_default=True,
        ),
    ]
