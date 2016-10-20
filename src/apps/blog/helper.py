
from django.db import transaction

from .models import Category, Author, Blog
from apps.blog import utils
from apps.blog import serializers


def get_blogs(blog_id=None):
    """
    It will return all blog details or perticular blog details
    """
    if blog_id:
        try:
            blog = Blog.objects.get(id=int(blog_id))
            serialized_blog = serializers.BlogDetailsSerializer(blog)
        except Blog.DoesNotExist:
            return None, "Enter valid blog id", None
    else:
        blogs = Blog.objects.all().order_by('id')
        serialized_blog = serializers.BlogDetailsSerializer(blogs, many=True)

    return True, "Success", serialized_blog.data


def validate_categories(category_ids):
    """
    Checking categories according to category ids
    """
    categories = []
    for category_id in category_ids:
        try:
            category = Category.objects.get(id=int(category_id))
            categories.append(category)
        except Category.DoesNotExist:
            return None, "{0} not a valid category id".format(category_id), None

    return True, "All Categories are valid", categories


def create_blog(title, slug, content, author_id=None, categories=None):
    """
    Create blog instance
    """
    blog = Blog()
    blog.title = title
    blog.slug = slug
    blog.content = content

    if author_id:
        try:
            author = Author.objects.get(id=int(author_id))
        except Author.DoesNotExist:
            return None, "Enter valid author id", None

        blog.author = author
    blog.save()

    if categories:
        blog.categories.add(*categories)

    serialized_blog = serializers.BlogDetailsSerializer(blog)
    return True, "Blog Successfully created", serialized_blog.data


def update_blog(blog_id, title, slug, content, author_id=None, categories=None):
    """
    Update blog according data
    """
    try:
        blog = Blog.objects.get(id=int(blog_id))
    except Blog.DoesNotExist:
        return None, "Enter valid Blog id", None

    if author_id:
        try:
            author = Author.objects.get(id=int(author_id))
        except Author.DoesNotExist:
            return None, "Enter valid author id", None

        blog.author = author

    if title:
        blog.title = title
    if slug:
        blog.slug = slug
    if content:
        blog.content = content
    blog.save()

    if categories is not None:
        current_categories = blog.categories.all()
        blog.categories.remove(*current_categories)
        blog.categories.add(*categories)

    serialized_blog = serializers.BlogDetailsSerializer(blog)
    return True, "Blog Successfully updated", serialized_blog.data


def delete_blog(blog_id):
    """
    For deleting blog for perticular blog_id
    """
    try:
        blog = Blog.objects.get(id=int(blog_id))
    except Blog.DoesNotExist:
        return None, "Enter valid Blog id"

    blog.delete()

    return True, "Blog Successfully Deleted"
