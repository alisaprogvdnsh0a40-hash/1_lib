from app.models import Book
import pytest

@pytest.fixture
def test_add_book():
    print('dar hal ezafe kardan detab')
    return Book('t','at',2000,'1_300',20)

def test_borrow(test_add_book):
   assert test_add_book.borrow_book()
