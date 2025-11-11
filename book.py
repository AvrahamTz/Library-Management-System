class Book:
    def __init__(self,title,author,ISBN):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.is_available=True
   
    def to_dict(self):
        return {"title":self.title
                ,"author":self.author
                ,"ISBN":self.ISBN
                ,"is_available":self.is_available}
    @staticmethod
    def from_dict(data: dict):
        return Book(
            book_id=data["book_id"],
            title=data["title"],
            author=data["author"],
            available=data["available"])
    
    def __str__(self):
        return F"title {self.title} author {self.author} ISBN {self.ISBN} is_available {self.is_available}"