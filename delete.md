from bookshelf.models import Book

# Delete the book
b = Book.objects.first()
b.delete()

Book.objects.all()
# Expected output:
# <QuerySet []>
