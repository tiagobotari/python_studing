"""
Python Strings - Immutable Sequences of Characters
====================================================
- Immutable: every operation creates a new string
- Unicode by default (Python 3)
- Hashable -> can be dict keys / set members
"""

# === Creation ===
s1 = "hello"
s2 = 'hello'
multiline = """line one
line two"""
raw = r"no\escape"                     # backslash is literal
f_string = f"2 + 3 = {2 + 3}"         # f-string interpolation

print("f_string:", f_string)
print("raw:", raw)

# === Immutability ===
s = "hello"
# s[0] = "H"  # TypeError: 'str' object does not support item assignment
s = "H" + s[1:]                        # creates a new string
print("\nmodified:", s)

# === Indexing & Slicing (same as lists) ===
s = "abcdef"
print("\ns[0]:", s[0])                  # 'a'
print("s[-1]:", s[-1])                  # 'f'
print("s[1:4]:", s[1:4])               # 'bcd'
print("s[::-1]:", s[::-1])             # 'fedcba' - reversed

# === Common Methods ===
s = "  Hello, World!  "

print("\nstrip:", repr(s.strip()))          # 'Hello, World!'
print("lstrip:", repr(s.lstrip()))         # 'Hello, World!  '
print("lower:", s.strip().lower())         # 'hello, world!'
print("upper:", s.strip().upper())         # 'HELLO, WORLD!'

s2 = "hello world"
print("\nsplit:", s2.split())              # ['hello', 'world']
print("split(','):", "a,b,c".split(","))  # ['a', 'b', 'c']
print("join:", "-".join(["a", "b", "c"])) # 'a-b-c'

print("\nreplace:", "aabaa".replace("a", "x"))      # 'xxbxx'
print("replace 1:", "aabaa".replace("a", "x", 1))   # 'xabaa'

print("\nfind:", "hello".find("ll"))       # 2 (index, or -1 if not found)
print("count:", "banana".count("an"))      # 2
print("startswith:", "hello".startswith("he"))  # True
print("endswith:", "hello".endswith("lo"))       # True

# === Checking Content ===
print("\nisdigit:", "123".isdigit())        # True
print("isalpha:", "abc".isalpha())          # True
print("isalnum:", "abc123".isalnum())       # True
print("isspace:", "   ".isspace())          # True
print("isupper:", "ABC".isupper())          # True
print("islower:", "abc".islower())          # True

# === String Building ===
# BAD: concatenation in a loop is O(n^2) because strings are immutable
# BAD: result = ""; for s in parts: result += s

# GOOD: join is O(n) total
parts = ["hello", "world", "python"]
result = " ".join(parts)
print("\njoined:", result)

# GOOD: list append + join
chars = []
for i in range(5):
    chars.append(str(i))
result = "".join(chars)
print("built:", result)

# === Formatting ===
name = "Alice"
age = 30

# f-strings (preferred, Python 3.6+)
print(f"\n{name} is {age} years old")
print(f"pi is {3.14159:.2f}")          # 2 decimal places
print(f"{'centered':^20}")             # center in 20 chars
print(f"{'left':<20}|")               # left align
print(f"{'right':>20}")               # right align

# .format()
print("{} is {}".format(name, age))

# === Character Conversion ===
print("\nord('a'):", ord("a"))          # 97 - char to int
print("chr(97):", chr(97))             # 'a' - int to char
print("ord('A'):", ord("A"))           # 65

# Useful for letter math
# e.g., 0-indexed position of letter: ord(ch) - ord('a')
print("position of 'c':", ord("c") - ord("a"))  # 2

# === Common Interview Patterns ===

# 1. Reverse a string
s = "hello"
print("\nreversed:", s[::-1])

# 2. Check palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print("palindrome:", is_palindrome("racecar"))

# 3. Character frequency
from collections import Counter
freq = Counter("abracadabra")
print("frequency:", freq)

# 4. Anagram check
def is_anagram(s, t):
    return Counter(s) == Counter(t)

print("anagram:", is_anagram("listen", "silent"))

# === Time Complexity Summary ===
# s[i]:         O(1)
# s + t:        O(len(s) + len(t)) - creates new string
# s in t:       O(len(s) * len(t)) worst case
# s.find(t):    O(len(s) * len(t)) worst case
# s.split():    O(n)
# s.join(lst):  O(total length)
# s.replace():  O(n)
# s.strip():    O(n)
# len(s):       O(1)
# s[::-1]:      O(n)

# === Interview Tips ===
# 1. Strings are IMMUTABLE -- concatenation in loops is O(n^2), use join
# 2. ord()/chr() for character arithmetic (letter positions, shifting)
# 3. s[::-1] for quick reversal
# 4. Counter for frequency problems, sorted() for anagram canonical form
# 5. split/join are the main tools for word-level manipulation
