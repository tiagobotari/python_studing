from solution import group_anagrams


def _normalize(groups: list[list[str]]) -> list[tuple[str, ...]]:
    """Sort each group and sort the list of groups for comparison."""
    return sorted(tuple(sorted(g)) for g in groups)


def test_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert _normalize(result) == _normalize(expected)


def test_empty_string():
    result = group_anagrams([""])
    assert _normalize(result) == _normalize([[""]])


def test_single_char():
    result = group_anagrams(["a"])
    assert _normalize(result) == _normalize([["a"]])


def test_no_anagrams():
    result = group_anagrams(["abc", "def", "ghi"])
    expected = [["abc"], ["def"], ["ghi"]]
    assert _normalize(result) == _normalize(expected)


def test_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    expected = [["abc", "bca", "cab"]]
    assert _normalize(result) == _normalize(expected)
