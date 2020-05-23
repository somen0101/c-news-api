from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Topics, Bookmark


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')


class NewsTopicsSerializer(serializers.ModelSerializer):
    """ A serializer for the PileColor model """
    class Meta:
        model = Topics
        fields = ('id', 'title', 'description', 'published_date',
                  'author', 'topic_url', 'image_url', 'top_news', 'domain_tags','sentimental')


class BookmarkSerializer(serializers.ModelSerializer):
    """ A serializer for the PileColor model """
    class Meta:
        model = Bookmark
        fields = ('id', 'username', 'title', 'description', 'published_date',
                  'author', 'topic_url', 'image_url', 'sentimental')