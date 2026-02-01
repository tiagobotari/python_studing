from solution import is_anagram


def test_valid_anagram():
    assert is_anagram("anagram", "nagaram") is True


def test_not_anagram():
    assert is_anagram("rat", "car") is False


def test_different_lengths():
    assert is_anagram("ab", "abc") is False


def test_empty_strings():
    assert is_anagram("", "") is True


def test_single_char():
    assert is_anagram("a", "a") is True


def test_repeated_chars():
    assert is_anagram("aab", "aba") is True


def test_same_chars_different_count():
    assert is_anagram("aacc", "ccac") is False
