from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Topics, Bookmark
from .serializers import UserSerializer, NewsTopicsSerializer, BookmarkSerializer


class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class NewsTopicsListCreate(generics.ListCreateAPIView):
    """ List and create  """
    queryset = Topics.objects.all()
    serializer_class = NewsTopicsSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Topics.objects.all().order_by('-top_news')
        domain = self.request.query_params.get('domain_tags', None)
        top = self.request.query_params.get('top_news', None)
        if domain and top is not None:
            queryset = queryset.filter(domain_tags=domain,top_news=top)
        elif top is None:
            queryset = queryset.filter(domain_tags=domain)
        return queryset


class NewsTopicsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update """
    queryset = Topics.objects.all()
    serializer_class = NewsTopicsSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BookmarkListCreate(generics.ListCreateAPIView):
    """ List and create """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Bookmark.objects.all()
        name = self.request.query_params.get('username', None)
        if name is not None:
            queryset = queryset.filter(username=name)
        return queryset

# Create your views here.
