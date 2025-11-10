managment={}
def menu():
    choise=None
    while choise != "4":
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Save & Exit")
        choise=input("Enter your choice: ")
        match choise:
            case "1":
                choise1=input("enter a book info ")
                pass
                print (f"book {choise1} added!")
            case "2":
                choise2=input("enter a user info ")
                pass
                print (f"user {choise2} added!")
            case "3":
                choise3=input("enter user id ")
                choise4=input("enter book ISBN")
                pass
                print(f"{User.__str__()}")
            case "4":
                print(f"{User.__str__()} ")
                choise3=input("enter user id ")
                choise4=input("enter book ISBN")
                pass
                print(f"return {choise4} book")
                
            case "5":
                list_available_books()
            
            case "6":
                title=input("enter book title ")
                search_book(title)
                
            

                
                