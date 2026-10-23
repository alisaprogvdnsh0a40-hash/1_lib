from app.models import Book
import pytest

#-------------------

@pytest.fixture
def test_book():
    print('dar hal ezafe kardan detab')
    return Book('t','at',2000,'1_300',20)

def test_borrow(test_book):
   assert test_book.borrow_book()
   print(test_book.total_copies,test_book.available_copies)
   assert test_book.total_copies > test_book.available_copies

# total_copies != total_copies + 1
def test_return(test_book):
    assert not test_book.return_book()

@pytest.mark.parametrize('num',[1,2,3,19])
def test_loop_borrow(test_book,num):
        
        print(num)
        for i in range(num):
            
            assert test_book.borrow_book()
            print(test_book.total_copies,test_book.available_copies)
            