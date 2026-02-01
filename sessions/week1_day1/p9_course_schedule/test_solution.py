from solution import can_finish


def test_simple_chain():
    assert can_finish(2, [[1, 0]]) is True


def test_cycle():
    assert can_finish(2, [[1, 0], [0, 1]]) is False


def test_no_prerequisites():
    assert can_finish(3, []) is True


def test_longer_chain():
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True


def test_longer_cycle():
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False


def test_diamond():
    # 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3 (no cycle)
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True


def test_single_course():
    assert can_finish(1, []) is True


def test_self_loop():
    assert can_finish(1, [[0, 0]]) is False
