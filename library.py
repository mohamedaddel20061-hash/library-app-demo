class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - [{status}]"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)


# --- Quick Test ---
if __name__ == "__main__":
    my_library = Library()
    b1 = Book("Clean Code", "Robert C. Martin", "12345")
    b2 = Book("The Pragmatic Programmer", "Andrew Hunt", "67890")

    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.list_books()