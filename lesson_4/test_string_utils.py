import pytest
from string_utils import StringUtils


@pytest.mark.parametrize('str1, result', [("alyona", "Alyona"),("a b", "A b"), ("Alyona", "Alyona"), ("a", "A")])
def test_positive_capitilise(str1, result):
    test_string = StringUtils()
    res = test_string.capitilize(str1)
    assert res == result

@pytest.mark.parametrize('str1, result', [("", ""), (" a", " a"), (" ", " ")])
def test_negative_capitilise(str1, result):
    test_string = StringUtils()
    res = test_string.capitilize(str1)
    assert res == result

def test_negative_capitilise_atribute():
    test_string = StringUtils()
    with pytest.raises(AttributeError):
        test_string.capitilize([None, 20])
    
@pytest.mark.parametrize('str1, result', [(" abc", "abc"), ("   abc", "abc"), ("a b c", "a b c"), (" a, b, c", "a, b, c")])    
def test_positive_trim(str1, result):
    test_string = StringUtils()
    res = test_string.trim(str1)
    assert res == result

@pytest.mark.parametrize('str1, result', [("", ""), (" ", ""), ("   ","")])
def test_negative_trim(str1, result):
    test_string = StringUtils()
    res = test_string.trim(str1)
    assert res == result

def test_negative_trim_atribute():
    test_string = StringUtils()
    with pytest.raises(AttributeError):
        test_string.trim([None, 20])

@pytest.mark.parametrize('str1, str2, result', [("a,b,c", ",", ["a", "b", "c"]), ("a:b:c", ":", ["a", "b", "c"]), ("a b c", " ", ["a", "b", "c"]), ("3;2;1", ";", ["3", "2", "1"])])
def test_positive_to_list(str1, str2, result):
    test_string = StringUtils()
    res = test_string.to_list(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("", "", [])])
def test_negative_to_list(str1, str2, result):
    test_string = StringUtils()
    res = test_string.to_list(str1, str2)
    assert res == result

@pytest.mark.xfail
def test_negative_to_list_detaled_1():
    test_string = StringUtils()
    res = test_string.to_list("1a2a3a", "a")
    assert res == ["1", "2", "3"]

@pytest.mark.xfail
def test_negative_to_list_detaled_2():
    test_string = StringUtils()
    res = test_string.to_list("a1b1c1", "1")
    assert res == ["a", "b", "c"]

def test_negative_to_list_detaled_None():
    test_string = StringUtils()
    with pytest.raises(AttributeError):
        test_string.to_list(None)

@pytest.mark.parametrize('str1, str2, result', [("Al", "A", True), ("al by", "b", True), ("al 1", "1", True ), ("Aly", "Aly", True), ("12", "12", True)] ) 
def test_positive_True_contains(str1, str2, result):
    test_string = StringUtils()
    res = test_string.contains(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("Alyona", "w", False), ("Alyona 2", "3", False)])
def test_positive_False_contains(str1, str2, result):
    test_string = StringUtils()
    res = test_string.contains(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("","", True), ("as,", ",", True), (" "," ",True), ("ALY", "aly", False)])
def test_negative_contains(str1, str2, result):
    test_string = StringUtils()
    res = test_string.contains(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("a", "a", ""), ("abc", "ab", "c"), ("123","1","23"), ("abc d", "d", "abc ")])
def test_positive_delete_symbol(str1, str2, result):
    test_string = StringUtils()
    res = test_string.delete_symbol(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("", "", ""), ("Alyona", "a", "Alyon"), ("AaBaCa", "a", "ABC"), ("1    1", " ", "11")])
def test_negative_delete_symbol(str1, str2, result):
    test_string = StringUtils()
    res = test_string.delete_symbol(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("Alyona", "A", True), ("abc", "a", True), ("123", "1", True), ("Alyona Bir", "Aly", True)])
def test_positive_True_starts_with(str1, str2, result):
    test_string = StringUtils()
    res = test_string.starts_with(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("Alyona", "S", False), ("abc", "ac", False)])
def test_positive_False_starts_with(str1, str2, result):
    test_string = StringUtils()
    res = test_string.starts_with(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("", "", True), (" ", " ", True), ("abc", "A", False), ("Abc", "abc", False), (".", ".", True)])
def test_negative_starts_with(str1, str2, result):
    test_string = StringUtils()
    res = test_string.starts_with(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("Alyona", "a", True), ("abc", "c", True), ("123", "3", True), ("Alyona Bir", "Bir", True)])
def test_positive_True_end_with(str1, str2, result):
    test_string = StringUtils()
    res = test_string.end_with(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("Alyona", "S", False), ("abc", "ac", False), ("123", "2", False)])
def test_positive_False_end_with(str1, str2, result):
    test_string = StringUtils()
    res = test_string.end_with(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, str2, result', [("", "", True), (" ", " ", True), ("abc", "C", False), ("Abc", "abc", False), (".", ".", True)])
def test_negative_end_with(str1, str2, result):
    test_string = StringUtils()
    res = test_string.end_with(str1, str2)
    assert res == result

@pytest.mark.parametrize('str1, result', [("", True), (" ", True), ("    ", True)])
def test_positive_True_is_empty(str1, result):
    test_string = StringUtils()
    res = test_string.is_empty(str1)
    assert res == result

@pytest.mark.parametrize('str1, result', [("abc", False), (".", False), ("123", False)])
def test_positive_False_is_empty(str1, result):
    test_string = StringUtils()
    res = test_string.is_empty(str1)
    assert res == result

@pytest.mark.parametrize('str1, result', [("  a  ", False), (" 1 ", False), (" . ", False)])
def test_negative_is_empty(str1, result):
    test_string = StringUtils()
    res = test_string.is_empty(str1)
    assert res == result

@pytest.mark.parametrize('str1,str2, result', [(["a","b","c"],",", "a,b,c"), (["1","2","3"],":", "1:2:3")])
def test_positive_list_to_string(str1,str2, result):
    test_string = StringUtils()
    res = test_string.list_to_string(str1,str2)
    assert res == result
    
@pytest.mark.parametrize('str1,str2, result', [([".",".","."], ",", ".,.,."), ([13,14,15],",","13,14,15"), (["","",""],":","::"), ([],"","")])
def test_negative_list_to_string(str1,str2, result):
    test_string = StringUtils()
    res = test_string.list_to_string(str1,str2)
    assert res == result