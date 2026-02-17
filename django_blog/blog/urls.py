from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from django.urls import path

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path("register/", views.register_view, name="register"), # type: ignore
    path("login/", views.login_view, name="login"), # type: ignore
    path("logout/", views.logout_view, name="logout"), # type: ignore
    path("profile/", views.profile_view, name="profile"),   # type: ignore
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
