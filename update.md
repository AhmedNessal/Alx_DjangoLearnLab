from bookshelf.models import Book

# Update the book title
b = Book.objects.first()
b.title = "Nineteen Eighty-Four"
b.save()

b.title
# Expected output:
# 'Nineteen Eighty-Four'
