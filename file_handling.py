import json
import user
import book
class File_handling:
    def save_data(self):
        data = {
            "books": [book.Book.to_dict() for b in self.books.values()],
            "users": [user.User.to_dict() for u in self.users.values()]
        }
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = {b["book_id"]: book.Book.from_dict(b) for b in data.get("books", [])}
                self.users = {u["user_id"]: user.User.from_dict(u) for u in data.get("users", [])}
        except FileNotFoundError:
            self.books = {}
            self.users = {}