class User:
    def __init__(self,name,ID,borrowed_books):
        self.name = name
        self.ID = ID
        self.borrowed_books = borrowed_books
    
    def __str__(self):
        return f"name {self.name} your ID {self.ID} borrowed {self.borrowed_books}"     
    