from app.models import Library,Guest,Member,Librarian
from app.exceptions import PermissionDenied
import pytest


#-------------------
@pytest.fixture
def test_library():
    print('library dar hal ezafe shodan')
    return Library()

def tests_p_library(test_library):
    guest1 = Guest(1,"ali","ali@")
    member1 = Member(2,"reza","reza@")
    librarian1 = Librarian(3,"hamid","hamid@")

    test_library.add_book(librarian1,"b1","author1",2000,"101_4",1)
    test_library.add_book(librarian1,"b2","author1",2000,"102_3",1)

    #with isbn test permission for guest and member :
    #guest
    with pytest.raises(PermissionDenied):
        test_library.borrow_book(book="101_4",user=guest1)    
    with pytest.raises(PermissionDenied):        
        test_library.add_book(guest1,"b2","author1",2000,"101_5",1)    
    #member
    with pytest.raises(PermissionDenied):                
        test_library.add_book(member1,"b3","author1",2000,"101_6",1)    
    #librarian
    test_library.add_book(librarian1,"b4","author1",2000,"101_7",1)    

     