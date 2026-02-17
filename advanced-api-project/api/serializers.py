from rest_framework import serializers
from datetime import date
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model data and validates publication year.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensures publication year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model and nests related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
