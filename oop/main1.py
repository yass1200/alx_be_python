from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)          # Calls __str__
    print(repr(my_book))    # Calls __repr__

    del my_book             # Triggers __del__

if __name__ == "__main__":
    main()
