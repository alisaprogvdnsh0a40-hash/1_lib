from app.models import Guest,Member,Librarian
import pytest

#-------------------

@pytest.fixture
def test_guest():
    print('user sakhte shod')
    return Guest(2,'ali2','@ali2')

def test_p_guest(test_guest):
    print(test_guest)
    assert len(test_guest.get_permissions()) == 1

#-------------------


@pytest.fixture
def test_member():
    print('user sakhte shod')
    return Member(3,'ali3','@ali3')

def test_p_member(test_member):
    print(test_member)
    assert len(test_member.get_permissions()) == 3

#-------------------

@pytest.fixture
def test_librarian():
    print('user sakhte shod')
    return Librarian(4,'ali4','@ali4')

def test_p_librarian(test_librarian):
    print(test_librarian)
    assert len(test_librarian.get_permissions()) == 5

