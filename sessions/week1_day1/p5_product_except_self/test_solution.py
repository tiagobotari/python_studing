from solution import product_except_self


def test_basic():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_with_zero():
    assert product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]


def test_two_zeros():
    assert product_except_self([0, 0, 2, 3]) == [0, 0, 0, 0]


def test_negative_numbers():
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_elements():
    assert product_except_self([2, 3]) == [3, 2]


def test_all_ones():
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]
