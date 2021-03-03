import pytest

@pytest.mark.parametrize("test_input,expected", [('a', '%a%'), ('%a', '%%a'), ('a%', '%a%')])
def test_str_1(test_input, expected):
    got_result = test_input.center(3, '%')
    assert got_result == expected


def test_str_2():
    string_with_spaces = '\n    \n \r'
    string_without_spaces = 'string'
    TrueValue = string_with_spaces.isspace()
    FalseValue = string_without_spaces.isspace()
    assert TrueValue == True and FalseValue == False


def test_str_3():
    string = 'john doe'
    reference_string = 'John Doe'
    capitalized_string = string.split()[0].capitalize() + ' ' + string.split()[1].capitalize()
    assert capitalized_string == reference_string


def test_list_1():
    a = 1
    reference_list = [ a, a, a, a, ]
    real_list = [a, a]*2
    assert reference_list == real_list


def test_list_2():
    straight_order_list = [1, 2, 3, 4]
    reference_list = [4, 3, 2, 1]
    reverced_list = straight_order_list
    reverced_list.reverse()
    assert reference_list == reverced_list


def test_list_3():
    reference_list = ['a', 'b', 'c']
    try:
        reference_list.remove('d')
    except ValueError:
        pass
