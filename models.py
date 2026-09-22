from exceptions import LibraryError,BookNotAvailable,BookNotFound,PermissionDenied
from meta import UserMeta
class Book:

    def __init__(self,title,author,year,isbn,total_copies):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def __repr__(self):
        return f"Book:{self.title}"
# ----------------
    def __eq__(self, other):
        if not isinstance(other,Book):
            return False
        return (self.isbn == other.isbn)
# ----------------

    def __str__(self):
        return f"zakhire shod : {self.title}| nevisande:{self.author}| sal va tedad copy:{self.year},{self.total_copies}|mojodi:{self.available_copies}/{self.total_copies}"

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("tedad copy ketab kam shod")
            return True
        else:
            print("tedad copy = 0!!")
            return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print("ketab bargasht dade shod")
            return True
        else:
            print("chetor be copy hay kamel in ketab mi afzaiid?")
            return False

class User(metaclass = UserMeta):
    def __init__(self,user_id,name,email):
        self.user_id = user_id
        self.name = name 
        self.email = email
        self.borrowed = 0

    def __repr__(self):
        return f"Person:{self.name}"
# ----------------
    def __eq__(self, other):
        if not isinstance(other,User):
            return False
        return (self.user_id == other.user_id)
# ----------------

    def __str__(self):
        return f"user{self.user_id}= {self.name}({self.email})ba tedad amanat {self.borrowed}"

class Guest(User):
    # def __init__(self, user_id, name, email):
    #     super().__init__(user_id, name, email)
    # def __str__(self):
    #     return f"user{self.user_id}= {self.name}({self.email})"
    def get_permissions(self):
        return ["view_books"]

class Member(User):
    # def __init__(self, user_id, name, email):
    #     super().__init__(user_id, name, email)
    # def __str__(self):
    #     return f"user{self.user_id}= {self.name}({self.email})"
    def get_permissions(self):
        return ["view_books","borrow_books","return_books"]


class Librarian(User):
    # def __init__(self, user_id, name, email):
    #     super().__init__(user_id, name, email)
    # def __str__(self):
    #     return f"user{self.user_id}= {self.name}({self.email})"
    def get_permissions(self):
        return ["view_books","borrow_books","return_books","add_book","remove_book"]





# print(guest1)
# print("mojavez ha",guest1.get_permissions())

# print(member1)
# print("mojavez ha",member1.get_permissions())

# print(librarian1)
# print("mojavez ha",librarian1.get_permissions())


class Library:

    def __init__(self):
        self.books = {}
        self.users = {}

    def add_user(self,user):
        self.users[user.user_id]=user
# ----------------

    def __str__(self):
        lu = len(self.users)
        lb = len(self.books)
        return f"lib ba tedad karbar:{lu},tedad anvae ketab:{lb}"
# ----------------

    def __len__(self):
        """ bargasht midahad books number"""
        return len(self.books)

    def len_users(self):
        """ bargasht midahad users number"""                
        return len(self.users)
# ----------------
    def __contains__(self, book):
        """Book object or isbn"""
        if isinstance(book,Book):
            return book.isbn in self.books
        elif isinstance(book,str):
            return book in self.books
        return False
# ----------------
    def __iter__(self):
        return iter(self.books.values())
# ----------------
    def __eq__(self, other):
        if not isinstance(other,Library):
            return False
        return (self.books == other.books) and (self.users == other.users)
# ----------------
    def __getitem__(self,id_or_isbn):
        if  isinstance(id_or_isbn,str):   
            if id_or_isbn not in self.books:
                raise BookNotFound("in ketab dar ketabkhaneh mojod nist")
            return self.books[id_or_isbn]    
        elif isinstance(id_or_isbn,int):
            if id_or_isbn not in self.users:
                raise LibraryError("in fard dar ketabkhaneh mojod nist")
            return self.users[id_or_isbn]    
# ----------------
    def add_book(self,title,author,year,isbn,total_copies):
        if isbn in self.books:
            raise LibraryError("in ketab wojod darad")
        new_book = Book(title,author,year,isbn,total_copies)
        self.books[isbn] = new_book
    def remove_book(self,isbn):            
        if not (isbn in self.books):
            raise LibraryError("in ketab mojod nist")
        print(f"ketab {self.books[isbn]} \n dar hal hazf...")
        del self.books[isbn]
        print("hazf shod")
    def increase_book(self,user,book,num):
        if len(user.get_permissions()) > 3:
            book.total_copies += num
            book.available_copies += num
            print(f"copys = {book.available_copies}/{book.total_copies}")
        else:
            raise PermissionDenied("shoma ejaze nadarid")


    def decrease_book(self,user,book,num):
        if len(user.get_permissions()) > 3:        
            if book.total_copies >= num :
                    book.total_copies -= num
                    book.available_copies -= num
                    print(f"copys = {book.available_copies}/{book.total_copies}")
            else:
                    raise BookNotAvailable("tedad ketab kafi nist")

        else:
            raise PermissionDenied("shoma ejaze nadarid")

    def borrow_book(self,user,book):
        if  len(user.get_permissions()) > 1:   
            if user.borrowed < 3 :    
                if book.borrow_book():
                    user.borrowed += 1
            else:
                raise LibraryError("zarfiat amanat shoma 3/3 ast")
        else:
            raise PermissionDenied("shoma ejaze nadarid")

    def return_book(self,user,book):
        if  len(user.get_permissions()) > 1:        
            if user.borrowed > 0 :
                if book.return_book():
    
                    user.borrowed -= 1    
            else:
                raise LibraryError("chizi baray bargardandan nadarid")

        else:
            raise PermissionDenied("shoma ejaze nadarid")

# try_raise_except or raise in def haye class ha, faramosh nashe!!
# def run0():
#     try:
#         Lib1 = Library()
#         b1 = Book("b1","author1",2000,101,1)
#         b2 = Book("b2","author1",2000,102,1)

#         guest1 = Guest("u1","ali","ali@gmail.com")
#         member1 = Member("u2","reza","reza@gmail.com")
#         librarian1 = Librarian("u3","hamid","hamid@gmail.com")

#         Lib1.add_book(b1)
#         Lib1.add_book(b2)

#         Lib1.add_user(guest1)
#         Lib1.add_user(member1)
#         Lib1.add_user(librarian1)

#         print(Lib1)

#         # Lib1.borrow_book(member1,b1)
#         # Lib1.borrow_book(member1,b1)

#         # print(member1)

#         # Lib1.decrease_book(librarian1,b1,4)
#         # print(b1.total_copies)
        
#         print(len(Lib1))
#         print(Lib1.len_users())
#         print(Lib1[101])
#         print(Lib1["u1"])
#         print(repr(b1))
#         print(repr(guest1))
    
#     except Exception as e:
        
#         print(type(e))
#         print(e)








