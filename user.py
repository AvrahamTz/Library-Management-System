class User:
    def __init__(self,name,ID,borrowed_books:list):
        self.name = name
        self.ID = ID
        self.borrowed_books = borrowed_books

    def to_dict(self):
        return{"name":self.name
               ,"id":self.id
               ,"borrowed_books":self.borrowed_books}
    @staticmethod
    def from_dict(data: dict):
        user = User(data["user_id"], data["name"])
        user.borrowed_books = data.get("borrowed_books", [])
        return user

    
    def __str__(self):
        return f"name {self.name} your ID {self.ID} borrowed {self.borrowed_books}"     
    