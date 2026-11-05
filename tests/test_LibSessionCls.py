from app.session import LibSession
import pytest
from app.models import Guest,Member,Librarian,Library
from app.exceptions import*

# -------------------

Lib1 = Library()
guest1 = Guest(1,"ali","ali@")
member1 = Member(2,"reza","reza@")
librarian1 = Librarian(3,"hamid","hamid@")

Lib1.add_book(librarian1,"b1","author1",2000,"101_4",1)
Lib1.add_book(librarian1,"b2","author1",2000,"102_3",1)

Lib1.add_user(guest1)

# without add member1 to Lib1
# Lib1.add_user(member1)

Lib1.add_user(librarian1)

# --------------------

def test_with_authentic_user():
    
    with LibSession(Lib1,guest1.user_id):
         pass

def test_without_authentic_user():
    
    with pytest.raises(UserNotFound):
        
        with LibSession(Lib1,member1.user_id):
            pass    