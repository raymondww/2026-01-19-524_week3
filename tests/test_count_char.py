import pytest

from pytest1.countchar import count_char
#from pytest1.countchar.count_char import count_char

def test_count_char():
    string = "hello"
    expected = 5
    actual = count_char.count_char(string)
    assert actual == expected

    string = ""
    expected = 0
    actual = count_char.count_char(string)
    assert actual == expected

    string = "Hello class of 524 section 1"
    expected = 28
    actual = count_char.count_char(string)
    assert actual == expected

def test_count_char_wrong_input():
    with pytest.raises(TypeError):
        count_char.count_char(123)
