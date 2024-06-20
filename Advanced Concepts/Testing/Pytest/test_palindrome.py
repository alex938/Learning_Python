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


'''
pip install pytest

PS C:\Users\Admin\Desktop> pytest -v
================================================================================= test session starts ================================================================================== 
platform win32 -- Python 3.12.1, pytest-8.2.2, pluggy-1.5.0 -- C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Admin\Desktop
collected 5 items

test_palindrome.py::test_simple_valid_palindrome PASSED                                                                                                                           [ 20%] 
test_palindrome.py::test_return_type_valid PASSED                                                                                                                                 [ 40%] 
test_palindrome.py::test_simple_invalid_raises_exception_on_notstring PASSED                                                                                                      [ 60%] 
test_palindrome.py::test_simple_valid_wrong_case_palindrome PASSED                                                                                                                [ 80%] 
test_palindrome.py::test_complex_palindrome_clean PASSED                                                                                                                          [100%] 

================================================================================== 5 passed in 0.04s ===================================================================================
'''
