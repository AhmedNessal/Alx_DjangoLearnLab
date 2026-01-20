
### 2️⃣ `retrieve.md`
```markdown
```python
from bookshelf.models import Book

Book.objects.all()
# Expected output:
# <QuerySet [<Book: 1984>]>

b = Book.objects.first()
b.title, b.author, b.publication_year
# Expected output:
# ('1984', 'George Orwell', 1949)
