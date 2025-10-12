class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor: Initialize the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Print a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a human-readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
