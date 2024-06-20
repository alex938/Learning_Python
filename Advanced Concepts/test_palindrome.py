import pytest
from Palindrome import Palindrome, NotStringError

@pytest.fixture
def simple_palindrome():
    """Returns a valid simple palindrome object"""
    return Palindrome("racecar")

def test_simple_valid_palindrome(simple_palindrome):
    assert simple_palindrome.is_palindrome() == True

def test_return_type_valid(simple_palindrome):
    assert isinstance(simple_palindrome.is_palindrome(), bool) == True

def test_simple_invalid_raises_exception_on_notstring():
    with pytest.raises(NotStringError):
        simplePal = Palindrome(10)

def test_simple_valid_wrong_case_palindrome():
    awkwardPal = Palindrome("RaCEcAr")
    assert awkwardPal.is_palindrome() == True

def test_complex_palindrome_clean():
    awkwardPal = Palindrome("R*a$1ce21122121car1221%$£!")
    assert awkwardPal.is_palindrome() == True
