from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Author, Book


class BookAPITestCase(TestCase):
    """Unit tests for Book API endpoints."""

    def setUp(self):
        """Create test data and users."""
        # Create an author
        self.author = Author.objects.create(name="Test Author")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2022,
            author=self.author
        )

        # Create users
        self.user = User.objects.create_user(username="user1", password="pass1234")
        self.client = APIClient()

    def test_list_books_anonymous(self):
        """Anyone can list books."""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_retrieve_book_anonymous(self):
        """Anyone can retrieve a single book."""
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book_unauthenticated(self):
        """Anonymous user cannot create a book."""
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated user can create a book."""
        self.client.login(username="user1", password="pass1234")
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "New Book")
        self.client.logout()

    def test_update_book_authenticated(self):
        """Authenticated user can update a book."""
        self.client.login(username="user1", password="pass1234")
        data = {"title": "Updated Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.put(f"/api/books/update/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")
        self.client.logout()

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book."""
        self.client.login(username="user1", password="pass1234")
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        self.client.logout()

    def test_filter_books(self):
        """Filter books by title."""
        response = self.client.get("/api/books/?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_search_books(self):
        """Search books by author name."""
        response = self.client.get("/api/books/?search=Test Author")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Order books by title."""
        Book.objects.create(title="Another Book", publication_year=2021, author=self.author)
        response = self.client.get("/api/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Another Book")
