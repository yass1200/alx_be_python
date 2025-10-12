class Book:
    """Base class representing a general book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Return a formatted string describing the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title, author, file_size):
        # Call base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a formatted string describing the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title, author, page_count):
        # Call base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a formatted string describing the printed book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A Library that contains and manages a collection of books."""
    def __init__(self):
        self.books = []  # Composition: list of Book, EBook, or PrintBook instances

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print the details of all books in the library."""
        for book in self.books:
            print(book)
