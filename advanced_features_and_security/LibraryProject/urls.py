from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views

urlpatterns = [
    path('books/view/', views.view_books, name='view_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/edit/', views.edit_book, name='edit_book'),
    path('books/delete/', views.delete_book, name='delete_book'),
    path("register/", views.register, name="register"), # type: ignore

    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout"
    ),

    path("books/", views.list_books, name="list_books"),

    path(
        "library/<int:pk>/",
        views.LibraryDetailView.as_view(),
        name="library_detail"
    ),
]
