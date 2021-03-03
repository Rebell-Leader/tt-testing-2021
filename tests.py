import pytest


def test_str_1():
    assert (1, 2, 3) == (1, 2, 3)


def test_str_2():
    pass


def test_str_3():
    pass


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
