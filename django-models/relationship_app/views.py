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
