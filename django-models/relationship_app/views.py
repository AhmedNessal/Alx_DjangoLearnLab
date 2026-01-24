from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Library
from .models import Book


def list_books(request):
    books = Book.objects.all()
    output = []

    for book in books:
        output.append(f"{book.title} by {book.author.name}")

    return HttpResponse("\n".join(output))


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
