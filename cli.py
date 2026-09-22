from models import*
from session import LibSession
from exceptions import*
import time
#-------run0---------
Lib1 = Library()
guest1 = Guest(1,"ali","ali@")
member1 = Member(2,"reza","reza@")
librarian1 = Librarian(3,"hamid","hamid@")

Lib1.add_book("b1","author1",2000,"101_4",1)
Lib1.add_book("b2","author1",2000,"102_3",1)

Lib1.add_user(guest1)
Lib1.add_user(member1)
Lib1.add_user(librarian1)
# -------------------------------------------------

def register1(semat):
    print("name karbari jadid:")
    name = str(input())
    print("email jadid:")
    email = str(input())            
    if semat == 3:
        new_user = Librarian(int(Lib1.len_users())+1,name,email)
        Lib1.add_user(new_user)
    elif semat == 2:
        new_user = Member(int(Lib1.len_users())+1,name,email)
        Lib1.add_user(new_user)
    elif semat == 1:
        new_user = Guest(int(Lib1.len_users())+1,name,email)
        Lib1.add_user(new_user)
    
def register0():
    print("------------Register-----------")
    print("adad semat ra vared konid  \n( Guest = 1 )  ( Member = 2 )  ( Librarian = 3 (password))")
    semat = int(input())    
    if semat == 3:
        print("password:")
        ps = int(input())
        if not ps == 1234:
            raise LibraryError("password nadorost ast")
        register1(3)
        
    elif semat==1 or semat == 2:
        register1(semat)    

    else:
        raise LibraryError("semat nadorost ast")
        

def login1(user_id):
    bool_ch = False
    with LibSession(Lib1,user_id):
        while not bool_ch:    
            print("........in your account........")    
            if isinstance(Lib1[user_id],Guest):
                print("adad delkhah ra vared konid \n"
                "( view_books = 1 )")
                key = int(input())
                
                if  not key == 1:            
                    raise LibraryError("adad nadorost ast")

                for book in Lib1:
                    print(book)
            


            elif isinstance(Lib1[user_id],Member):
                print("adad semat ra vared konid  \n"
                "( view_books = 1 )  ( borrow_books = 2 )  ( return_books = 3 )")
                key = int(input())
                if key == 1:
                    for book in Lib1:
                        print(book)
                elif key == 2:
                    print("shabak ketab:")
                    shabak = str(input())
                    if not (shabak in Lib1):
                        raise LibraryError("shabak peyda nashod")
                    Lib1.borrow_book(Lib1[user_id],Lib1[shabak])
                elif key == 3:
                    print("shabak ketab:")
                    shabak = str(input())
                    if not (shabak in Lib1):
                        raise LibraryError("shabak peyda nashod")
                    Lib1.return_book(Lib1[user_id],Lib1[shabak])

            elif isinstance(Lib1[user_id],Librarian):
                print("adad semat ra vared konid  \n"
                "( view_books = 1 )  ( borrow_books = 2 )  ( return_books = 3 ) \n" \
                "( add_book= 4 ) ( remove_book= 5 )")
                key = int(input())
                if key == 1:
                    for book in Lib1:
                        print(book)
                elif key == 2:
                    print("shabak ketab:")
                    shabak = str(input())
                    if not (shabak in Lib1):
                        raise LibraryError("shabak peyda nashod")
                    Lib1.borrow_book(Lib1[user_id],Lib1[shabak])
                elif key == 3:
                    print("shabak ketab:")
                    shabak = str(input())
                    if not (shabak in Lib1):
                        raise LibraryError("shabak peyda nashod")
                    Lib1.return_book(Lib1[user_id],Lib1[shabak])
                elif key == 4:
                    print("title:")
                    title = str(input())
                    print("author:")
                    author = str(input())

                    print("year:")
                    year = str(input())

                    print("shabak:")
                    shabak = str(input())

                    print("total_copies:")
                    total_copies = int(input())
                    Lib1.add_book(title,author,year,shabak,total_copies)
                elif key == 5:
                    
                    print("shabak:")
                    shabak = str(input())

                    Lib1.remove_book(shabak)

            print("barmigardid be meno?\n (na = 0),(bale =1)")
            choice = int(input())
            if not ((choice == 0) or (choice == 1)):
                raise LibraryError("vorodi 0 ya 1") 
            bool_ch = bool(choice)
    
def login0():
    print("------------Login-----------")
    print("name karbari:")
    name = str(input())
    print("email:")
    email = str(input())            
    user_pass = False

    for user in Lib1.users.values():
        print(user.name,user.email)
        print((user.name == name),(user.email == email))
        if (user.name == name) and (user.email == email):
            user_pass = True
            user_id = user.user_id
            break
    print(user_pass)
    if not user_pass :
        raise UserNotFound("user ba in moshakhasat peida nashod") 
    login1(user_id)

def run1():
    try:

        while True:
            print("------------Library_cli-----------")
            print("benevisid 1 baray login , 2 baray register , 3 off")
            key = int(input())
            if key == 1:
                login0()
            elif key == 2:
                register0()
            elif key == 3: 
                print("------------Exit-----------")
                break
            else:
                raise LibraryError("vorodi na motabar")

    except Exception as e:
        print(f"error {type(e)} : {e}") 

run1()