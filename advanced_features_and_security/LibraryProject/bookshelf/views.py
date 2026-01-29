"""
Security Best Practices Implemented:

1. DEBUG=False to prevent debug info leakage.
2. SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF set.
3. CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE enforce HTTPS cookies.
4. CSRF tokens added in all POST forms.
5. All database queries use Django ORM to prevent SQL injection.
6. CSP headers added via middleware or in views to reduce XSS risk.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q
from .forms import ExampleForm

# -------------------------
# Book Views with Permissions
# -------------------------

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    search_query = request.GET.get('q', '')  # Get search query safely
    if search_query:
        # Use Django ORM to avoid SQL injection
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("You have permission to add a book.")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return HttpResponse("You have permission to edit a book.")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("You have permission to delete a book.")
