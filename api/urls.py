from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view()),

    path('newstopics/', NewsTopicsListCreate.as_view()),
    path('newstopics/<pk>/', NewsTopicsRetrieveUpdate.as_view()),

    path('bookmark/', BookmarkListCreate.as_view()),
    path('bookmark/<username>', BookmarkListCreate.as_view()),
    path('bookmark/<username>/<pk>', BookmarkDestory.as_view()),

]