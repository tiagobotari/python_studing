"""
Python Tuples - Immutable Sequences
====================================
- Ordered, immutable sequence
- Hashable (if all elements are hashable) -> can be dict keys / set members
- Slightly faster than lists for iteration
"""

# === Creation ===
empty = ()
single = (42,)                         # comma is required for single element!
not_a_tuple = (42)                     # this is just int 42
from_literal = (1, 2, 3)
from_constructor = tuple([1, 2, 3])
from_string = tuple("abc")            # ('a', 'b', 'c')

print("single:", single, "type:", type(single))
print("not_a_tuple:", not_a_tuple, "type:", type(not_a_tuple))

# === Immutability ===
t = (1, 2, 3)
# t[0] = 99  # TypeError: 'tuple' object does not support item assignment

# But mutable objects INSIDE a tuple can still change
t2 = ([1, 2], [3, 4])
t2[0].append(99)
print("\nmutable inside tuple:", t2)  # ([1, 2, 99], [3, 4])

# === Packing & Unpacking ===
# Packing
point = 3, 4, 5         # parentheses optional
print("\npacked:", point)

# Unpacking
x, y, z = point
print("unpacked:", x, y, z)

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print("first:", first, "rest:", rest)   # first: 1 rest: [2, 3, 4, 5]

*start, last = (1, 2, 3, 4, 5)
print("start:", start, "last:", last)   # start: [1, 2, 3, 4] last: 5

# Swap values (tuple packing/unpacking)
a, b = 1, 2
a, b = b, a
print("swapped:", a, b)  # 2, 1

# === As Dict Keys (hashable) ===
# Tuples can be dict keys because they're immutable
grid_cache = {}
grid_cache[(0, 0)] = "start"
grid_cache[(1, 2)] = "visited"
print("\ngrid_cache:", grid_cache)

# Common pattern: using tuple as composite key
# e.g., memoization with multiple parameters
memo = {}
memo[(3, 5)] = 8   # cache result for args (3, 5)

# === Named Tuples ===
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print("\nnamed tuple:", p)
print("p.x:", p.x, "p[0]:", p[0])   # both work

# Named tuples are still immutable
# p.x = 10  # AttributeError

# _replace creates a new namedtuple with some fields changed
p2 = p._replace(x=10)
print("replaced:", p2)

# === Comparison ===
# Tuples compare element by element (lexicographic)
print("\n(1, 2) < (1, 3):", (1, 2) < (1, 3))    # True
print("(1, 2) < (2, 0):", (1, 2) < (2, 0))      # True (first element wins)

# Useful for sorting by multiple criteria
students = [("Alice", 90), ("Bob", 85), ("Charlie", 90)]
# Sort by grade descending, then name ascending
students.sort(key=lambda s: (-s[1], s[0]))
print("sorted students:", students)

# === Returning Multiple Values ===
def min_max(lst):
    return min(lst), max(lst)         # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5])
print("\nmin:", lo, "max:", hi)

# === Methods ===
t = (1, 2, 3, 2, 2)
print("\ncount of 2:", t.count(2))     # 3
print("index of 3:", t.index(3))       # 2

# === Time Complexity Summary ===
# index(x):    O(n)
# count(x):    O(n)
# x in tuple:  O(n)
# len():       O(1)
# Iteration:   O(n)
# Creation:    O(n)

# === Interview Tips ===
# 1. Use tuples for fixed collections (coordinates, RGB, DB rows)
# 2. Tuples as dict keys is a common pattern for caching/memoization
# 3. Function returning multiple values -> tuple unpacking
# 4. Tuple comparison is lexicographic -> useful for multi-key sorting
