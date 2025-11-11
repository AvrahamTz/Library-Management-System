
from book import Book
from user import User

class Library:
    def __init__(self, list_of_books: list, list_of_users: list):
        self.list_of_books = list_of_books
        self.list_of_users = list_of_users

    def add_book(self, new_book: Book):
        self.list_of_books.append(new_book)

    def add_user(self, new_user: User):
        self.list_of_users.append(new_user)

    def borrow_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn and book.is_available:
                for user in self.list_of_users:
                    if user.id == user_id:
                        book.is_available = False
                        user.borrowed_books.append(book_isbn)
                        print(f"{user.name} borrowed {book.title}")
                        return
        else:
            print("Book not available or user not found.")

    def return_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn and not book.is_available:
                for user in self.list_of_users:
                    if user.id == user_id and book_isbn in user.borrowed_books:
                        user.borrowed_books.remove(book_isbn)
                        book.is_available = True
                        print(f"{user.name} returned {book.title}")
                        return
        else:
            print("Return failed (book not borrowed or wrong user).")

    def list_available_books(self):
        print("Available books:")
        for book in self.list_of_books:
            if book.is_available:
                print(f"- {book.title} by {book.author} (ISBN {book.ISBN})")

    def search_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                return print("book found")
                
            else:    
                return print("Book not found.")
    
   

user1 = User("a", 1, [])
user2 = User("b", 2, [])
user3 = User("c", 3, [])

book1 = Book("abc", "abc", 1234)
book2 = Book("def", "DEF", 456)

users = [user1, user2]
books = [book1, book2]

library = Library(books, users)
library.add_book(Book("ggg", "zzz", 789))
library.add_user(user3)
library.borrow_book(1, 1234)
library.return_book(1, 1234)
library.list_available_books()
library.search_book("abd")



