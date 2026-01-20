from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")

    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book3)

    Librarian.objects.create(name="Alice", library=library1)

def run_queries():
    # Query all books by a specific author
    orwell = Author.objects.get(name="George Orwell")
    print("Books by George Orwell:", list(orwell.books.all()))

    # List all books in a library
    library = Library.objects.get(name="Central Library")
    print("Books in Central Library:", list(library.books.all()))

    # Retrieve the librarian for a library
    print("Librarian of Central Library:", library.librarian)
