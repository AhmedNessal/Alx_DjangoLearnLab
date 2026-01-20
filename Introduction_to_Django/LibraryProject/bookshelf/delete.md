from bookshelf.models import Book

# Retrieve the book first
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

Book.objects.all()
# Expected output:
# <QuerySet []>
