# Custom exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book class
class Book:
    def init(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def str(self):
        return f"'{self.title}' by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

# Member class
class Member:
    MAX_BORROW_LIMIT = 3

    def init(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} has already borrowed {self.MAX_BORROW_LIMIT} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed by someone else.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} successfully borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def str(self):
        borrowed_titles = ", ".join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"Member: {self.name}, Borrowed Books: {borrowed_titles}"

# Library class
class Library:
    def init(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")

        if not member:
            print(f"Member '{member_name}' not found in the library.")
            return
        
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if not book or not member:
            print(f"Invalid return attempt. Check member or book details.")
            return
        
        member.return_book(book)

    def show_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
    
    def show_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)

# Testing the system
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    library.add_member(Member("Alice"))
    library.add_member(Member("Bob"))

    try:
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Bob", "1984")
        library.borrow_book("Alice", "1984")  # Should raise an exception
    except Exception as e:
        print(f"Error: {e}")

    library.show_books()
    library.show_members()