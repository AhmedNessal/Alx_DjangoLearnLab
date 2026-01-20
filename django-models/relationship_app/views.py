from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # will be used in template

    # Optional: override get_object if you want to use query param
    def get_object(self):
        # e.g., library_id passed in URL
        return get_object_or_404(Library, id=self.kwargs['pk'])
