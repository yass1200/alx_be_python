# programming_paradigm/library_management.py

class Book:
    """Represents a book with a title, author, and checkout state."""
    def __init__(self, title, author):
        self.title = title               # public
        self.author = author             # public
        self._is_checked_out = False     # private-ish (convention)

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out

    def check_out(self):
        """Mark the book as checked out if available. Return True on success."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as available. Return True if it was checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True


class Library:
    """Manages a collection of Book instances."""
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def _find_by_title(self, title):
        """Return the first Book matching the title (exact match), else None."""
        for bk in self._books:
            if bk.title == title:
                return bk
        return None

    def check_out_book(self, title):
        """Check out a book by title. Return True on success, False otherwise."""
        book = self._find_by_title(title)
        if book:
            return book.check_out()
        return False

    def return_book(self, title):
        """Return a book by title. Return True on success, False otherwise."""
        book = self._find_by_title(title)
        if book:
            return book.return_book()
        return False

    def list_available_books(self):
        """Print available books as 'Title by Author' (one per line)."""
        for bk in self._books:
            if bk.is_available():
                print(f"{bk.title} by {bk.author}")
