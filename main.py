from library import Library
from book import Book
from user import User
user1 = User("a", 1, [])
user2 = User("b", 2, [])
user3 = User("c", 3, [])

book1 = Book("abc", "abc", 1234)
book3=Book("www","www",789)
book2 = Book("def", "def", 456)

users = [user1, user2]
books = [book2, book1,book3]

library = Library(books, users)
def menu():
    choise=None
    while choise != "7":
        print("")
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. return book\n5.show list of available books\n6.search book")
        choise=input("Enter your choice: ")
        match choise:
            case "1":
                choise1=input("enter a book info ")
                library.add_book(choise1)
                print (f"book {choise1} added!")
            case "2":
                choise2=input("enter a user info ")
                library.add_user(choise2)
                print (f"user {choise2} added!")
            case "3":
                choise3=int(input("enter user id "))
                
                choise4=int(input("enter book ISBN"))
                library.borrow_book(choise3,choise4)
                
            case "4":
                choise3=input("enter user id ")
                choise4=input("enter book ISBN")
                library.return_book(choise3,choise4)

            case "5":
                
                library.list_available_books()
                
                
            
            case "6":
                title=input("enter book title ")
                library.search_book(title)
                
            case "7":
                break

                
                