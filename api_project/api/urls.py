from django.contrib import admin
from django.urls import path, include

from api_project.api.views import BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
