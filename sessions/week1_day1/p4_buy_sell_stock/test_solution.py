from solution import max_profit


def test_basic():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_no_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_single_day():
    assert max_profit([5]) == 0


def test_two_days_profit():
    assert max_profit([1, 5]) == 4


def test_two_days_no_profit():
    assert max_profit([5, 1]) == 0


def test_profit_at_end():
    assert max_profit([2, 4, 1, 7]) == 6


def test_all_same():
    assert max_profit([3, 3, 3, 3]) == 0
