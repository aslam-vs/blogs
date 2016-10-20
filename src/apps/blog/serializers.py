from rest_framework import serializers
from .models import Category, Author, Blog


class BlogDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for blog details
    """
    author_name = serializers.SerializerMethodField()
    categories_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        if obj.author:
            return obj.author.name
        else:
            return None

    def get_categories_name(self, obj):
        if obj.categories:
            return obj.categories.values_list('title', flat=True)
        else:
            return None

    class Meta:
        model = Blog
        fields = ('id', 'title', 'slug', 'author', 'body', 'publish', 'created', 'modified',
                  'categories', 'author_name', 'categories_name')
