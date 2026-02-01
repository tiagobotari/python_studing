"""
Problem 2: Valid Anagram (LeetCode #242)
https://leetcode.com/problems/valid-anagram/

Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
and False otherwise.

Example:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False
"""


def is_anagram(s: str, t: str) -> bool:
    """ Given two strings return true if s is a anagram of t
    false otherwise. 

    Args:
        s (str): _description_
        t (str): _description_

    Returns:
        bool: _description_
    """
    def count_letters_word(word: str) -> dict[str, int]:
        count_letter_word = {}
        for letter in word:
            if letter in count_letter_word:
                count_letter_word[letter] += 1
            else:
                count_letter_word[letter] = 1
        return count_letter_word
    
    if len(s) != len(t): 
        return False
    
    count_s = count_letters_word(s)
    count_t = count_letters_word(t)
    print(count_s)
    print(count_t)
    return count_s == count_t


from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    """Implementation of is_anagram with Counter
    from collections

    Args:
        s (string): _description_
        t (str): _description_

    Returns:
        bool: _description_
    """
    return Counter(s) == Counter(t)


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    letter_count = {}
    for s_i, t_i in zip(s, t):
        letter_count[s_i] = letter_count.get(s_i, 0) + 1
        letter_count[t_i] = letter_count.get(t_i, 0) - 1
    
    for val in letter_count.values():
        if val != 0:
            return False
    
    return True 

a = {"test": 0}
print(a.pop(1, "do not exist"))