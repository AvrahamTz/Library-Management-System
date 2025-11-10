class Libarty:
    def __init__(self):
        pass
    def borrow_book(user_id, book_isbn):
        for i in range(len(managment['list_of_users'])):
            if user_id in managment['list_of_users'][i]['ID']:
                for i in range(len(managment['list_of_books'])):
                    if book_isbn in  managment['list_of_books'][i]['ISBN']  and borrow_book == False:
                        borrow_book = True
                        managment['list_of_books'][i]['is_available'] = False
            else:
                return "no such book"
    def return_book(user_id, book_isbn):
         for i in range(len(managment['list_of_users'])):
            if user_id in managment['list_of_users'][i]['ID']:
                for i in range(len(managment['list_of_books'])):
                    if book_isbn in  managment['list_of_books'][i]['ISBN']  and borrow_book == True:
                        borrow_book = False
                        managment['list_of_books'][i]['is_available'] = True
            else:
                return "check again your ID or book ISBN"



            