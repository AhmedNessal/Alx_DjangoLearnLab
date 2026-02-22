from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed_view
from .views import FeedView

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('feed/', feed_view, name='user-feed'),
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
]