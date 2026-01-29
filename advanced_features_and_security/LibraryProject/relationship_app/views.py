"""
Permissions & Groups Setup:

Custom permissions (can_view, can_create, can_edit, can_delete)
are defined in the Book model (relationship_app/models.py).

Groups are managed via Django Admin:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Views are protected using Django's @permission_required decorator.
""" 

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from .models import Library, Book # type: ignore
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return HttpResponse("Book added successfully")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id): # type: ignore
    return HttpResponse(f"Book {book_id} edited successfully")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id): # type: ignore
    return HttpResponse(f"Book {book_id} deleted successfully")

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

def list_books(request):
    books = Book.objects.all()
    output = []

    for book in books:
        output.append(f"{book.title} by {book.author.name}") # type: ignore

    return HttpResponse("\n".join(output))
@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    return HttpResponse("You can view books.")


@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("You can create a book.")


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request):
    return HttpResponse("You can edit a book.")


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("You can delete a book.")

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
