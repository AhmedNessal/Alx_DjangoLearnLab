from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
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
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    print(f"Books by {author_name}:", list(author.books.all()))

    # List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"Books in {library_name}:", list(library.books.all()))

    # Retrieve the librarian for a library
    print(f"Librarian of {library_name}:", library.librarian)
