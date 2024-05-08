import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('str1, result', [("alyona", "Alyona"), ("Alyona", "Alyona"), ("a", "A")])
def test_positive_capitilise(str1, result):
    test_string = StringUtils()
    res = test_string.capitilize(str1)
    assert res == result
@pytest.mark
def test_negative_capitilise():
    test_string = StringUtils()
    res = test_string.capitilize("2алена")
    assert res == "2Алена"

def test_positive_trim():
    test_string = StringUtils()
    res = test_string.trim(" abc")
    assert res == "abc"

def test_positive_to_list():
    test_string = StringUtils()
    res = test_string.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]

def test_positive_True_contains():
    test_string = StringUtils()
    res = test_string.contains("Alyona", "l")
    assert res == True

def test_positive_False_contains():
    test_string = StringUtils()
    res = test_string.contains("Alyona", "q")
    assert res == False

def test_negative_contains():
    test_string = StringUtils()
    res = test_string.contains("", "")
    assert res == True

def test_positive_delete_symbol():
    test_string = StringUtils()
    res = test_string.delete_symbol("AlyBir", "Aly")
    assert res == "Bir"

def test_negative_delete_symbol():
    test_string = StringUtils()
    res = test_string.delete_symbol("AlyBir", "ABC")
    assert res == "AlyBir"

def test_positive_starts_with():
    test_string = StringUtils()
    res = test_string.starts_with("Alyona", "A")
    assert res == True

def test_negative_starts_with():
    test_string = StringUtils()
    res = test_string.starts_with("Alyona", "a")
    assert res == False

def test_positive_end_with():
    test_string = StringUtils()
    res = test_string.end_with("Alyona", "a")
    assert res == True

def test_negative_starts_with():
    test_string = StringUtils()
    res = test_string.starts_with("Alyona", "")
    assert res == True

def test_positive_is_empty():
    test_string = StringUtils()
    res = test_string.is_empty("")
    assert res == True

def test_positive_is_empty():
    test_string = StringUtils()
    res = test_string.is_empty(" ")
    assert res == True

def test_positive_is_empty():
    test_string = StringUtils()
    res = test_string.is_empty("Alyona")
    assert res == False

def test_positive_list_to_string():
    test_string = StringUtils()
    res = test_string.list_to_string(["a","b","c","d"])
    assert res == "a, b, c, d"