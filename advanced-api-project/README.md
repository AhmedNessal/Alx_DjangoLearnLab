## API Views Overview

### Book Views
This project uses Django REST Framework generic views to handle CRUD operations for the Book model.

- **BookListView**
  - Endpoint: `/api/books/`
  - Method: GET
  - Access: Public (read-only)

- **BookDetailView**
  - Endpoint: `/api/books/<id>/`
  - Method: GET
  - Access: Public

- **BookCreateView**
  - Endpoint: `/api/books/create/`
  - Method: POST
  - Access: Authenticated users only

- **BookUpdateView**
  - Endpoint: `/api/books/<id>/update/`
  - Method: PUT / PATCH
  - Access: Authenticated users only

- **BookDeleteView**
  - Endpoint: `/api/books/<id>/delete/`
  - Method: DELETE
  - Access: Authenticated users only

### Permissions
Permissions are enforced using Django REST Framework permission classes.
Unauthenticated users have read-only access, while authenticated users can create, update, and delete records.

## Filtering, Searching, and Ordering

The BookListView supports advanced query features using Django REST Framework.

### Filtering
Implemented using DjangoFilterBackend.
Supported fields:
- title
- publication_year
- author

Example:
GET /api/books/?publication_year=2022

### Searching
Implemented using SearchFilter.
Searchable fields:
- title
- author name

Example:
GET /api/books/?search=django

### Ordering
Implemented using OrderingFilter.
Orderable fields:
- title
- publication_year

Example:
GET /api/books/?ordering=-publication_year
