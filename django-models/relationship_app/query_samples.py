from relationship_app.models import Author, Book, Library, Librarian

# Sample data creation
def create_sample_data():
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")

    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book3)

    librarian1 = Librarian.objects.create(name="Alice", library=library1)

# Queries
def run_queries():
    # Query all books by George Orwell
    orwell = Author.objects.get(name="George Orwell")
    books_by_orwell = orwell.books.all()  # type: ignore
    print("Books by George Orwell:", books_by_orwell)

    # List all books in Central Library
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print("Books in Central Library:", books_in_library)

    # Retrieve the librarian for Central Library
    librarian = library.librarian  # type: ignore
    print("Librarian of Central Library:", librarian)

if __name__ == "__main__":
    run_queries()
