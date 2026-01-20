from django.contrib import admin
from .models import Book

# Register the Book model with admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a search box for title and author
    search_fields = ('title', 'author')
    
    # Add filters for publication year
    list_filter = ('publication_year',)
