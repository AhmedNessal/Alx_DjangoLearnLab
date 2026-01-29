from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

# -------------------------
# Book Views with Permissions
# -------------------------

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    output = [f"{book.title} by {book.author}" for book in books]
    return HttpResponse("\n".join(output))


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("You have permission to add a book.")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return HttpResponse("You have permission to edit a book.")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("You have permission to delete a book.")
