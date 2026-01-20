from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    # Authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")

    # Books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter", author=author2)

    # Library
    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book3)

    # Librarian
    Librarian.objects.create(name="Alice", library=library1)

def run_queries():
    # Query all books by George Orwell
    orwell = Author.objects.get(name="George Orwell")
    print("Books by George Orwell:", list(orwell.books.all()))  # type: ignore

    # List all books in Central Library
    library = Library.objects.get(name="Central Library")
    print("Books in Central Library:", list(library.books.all()))

    # Retrieve the librarian for Central Library
    print("Librarian of Central Library:", library.librarian)  # type: ignore
