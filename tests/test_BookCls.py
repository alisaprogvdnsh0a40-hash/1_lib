from app.models import Book
import pytest

#-------------------

@pytest.fixture
def test_book2():
     print('dar hal ezafe kardan detab')
     return Book('t2','at2',2000,'2_300',20)

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


def test_equality_books(test_book,test_book2):
     assert test_book == test_book
     assert test_book != test_book2

def test_invalid_number_of_book():
     with pytest.raises(TypeError):
        b1 = Book('b1','b1a',2000,'1_450','hi')
     with pytest.raises(ValueError):
        b2 = Book('b2','b2a',2000,'1_460',-20)    