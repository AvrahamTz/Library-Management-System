class Library:
    def __init__(self,list_of_users:list,list_of_books:list):
        self.list_of_users=list_of_users
        self.list_of_books=list_of_books
        
    def add_book(self,new_book):
        self.list_of_books.append(new_book)
        return self.list_of_books
    
    def add_user(self,user):
        
        self.list_of_users.append(user)
        return self.list_of_users

    def list_available_books(self):
        return self.list_of_books
    
    def search_book(self,title):
        title=input("enter a book title ")
        if title in library_mangment["title"]:
            return "is avalible"
        else:
            return "not avalible"
            
