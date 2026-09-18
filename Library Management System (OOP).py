class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] '{self.title}' by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book with ID {book_id} already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        print(f"Added book: '{title}'")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Removed book: '{removed.title}'")
        else:
            print("Book not found.")

    def issue_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
        elif book.is_issued:
            print(f"'{book.title}' is already issued.")
        else:
            book.is_issued = True
            print(f"Successfully issued '{book.title}'.")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
        elif not book.is_issued:
            print(f"'{book.title}' was not issued.")
        else:
            book.is_issued = False
            print(f"Successfully returned '{book.title}'.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return
        print("\n--- Library Catalog ---")
        for book in self.books.values():
            print(book)


lib = Library()
lib.add_book("B101", "Python Crash Course", "Eric Matthes")
lib.add_book("B102", "Automate the Boring Stuff", "Al Sweigart")
lib.display_books()
lib.issue_book("B101")
lib.return_book("B101")