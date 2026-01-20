```markdown
```python
from bookshelf.models import Book

b = Book.objects.first()
b.title = "Nineteen Eighty-Four"
b.save()

b.title
# Expected output:
# 'Nineteen Eighty-Four'
