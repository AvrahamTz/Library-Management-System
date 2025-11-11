from book import Book
class User:
    def __init__(self,name, id,borrowed_books:list[Book]):
        self.name=name
        self.id=id
        self.borrowed_books=borrowed_books
    def to_dict(self):
        return{"name":self.name
               ,"id":self.id
               ,"borrowed_books":self.borrowed_books}