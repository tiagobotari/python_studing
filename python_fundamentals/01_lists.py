"""
Python Lists - Dynamic Arrays
==============================
- Ordered, mutable sequence
- Backed by a dynamic array (not a linked list)
- Heterogeneous (can mix types, but rarely should)
"""

# === Creation ===
empty = []
from_literal = [1, 2, 3]
from_constructor = list("abc")        # ['a', 'b', 'c']
from_range = list(range(5))           # [0, 1, 2, 3, 4]
repeated = [0] * 5                    # [0, 0, 0, 0, 0]

print("from_constructor:", from_constructor)
print("from_range:", from_range)

# === Indexing & Slicing ===
nums = [10, 20, 30, 40, 50]
print("\nnums[0]:", nums[0])           # 10
print("nums[-1]:", nums[-1])           # 50
print("nums[1:3]:", nums[1:3])         # [20, 30]
print("nums[::2]:", nums[::2])         # [10, 30, 50]  - every 2nd element
print("nums[::-1]:", nums[::-1])       # [50, 40, 30, 20, 10] - reversed

# Slicing creates a shallow copy
copy = nums[:]
copy[0] = 999
print("original unchanged:", nums[0])  # 10

# === Common Methods & Time Complexity ===
arr = [3, 1, 4, 1, 5]

arr.append(9)           # O(1) amortized - add to end
arr.insert(0, 99)       # O(n) - shifts all elements right
arr.pop()               # O(1) - remove from end
arr.pop(0)              # O(n) - remove from front, shifts left
arr.remove(1)           # O(n) - removes first occurrence of value 1
arr.extend([7, 8])      # O(k) where k is length of iterable
arr.reverse()           # O(n) - in-place
arr.sort()              # O(n log n) - Timsort, in-place, stable

print("\nafter operations:", arr)

# === Membership & Search ===
arr = [10, 20, 30, 40]
print("\n20 in arr:", 20 in arr)         # O(n) linear scan
print("index of 30:", arr.index(30))     # O(n) - raises ValueError if missing
print("count of 10:", arr.count(10))     # O(n)

# === Sorting ===
data = [3, 1, 4, 1, 5, 9]

sorted_copy = sorted(data)              # returns new list, original unchanged
data.sort()                             # sorts in-place, returns None

# Sort with key function
words = ["banana", "apple", "cherry"]
print("\nsorted by length:", sorted(words, key=len))
print("sorted reverse:", sorted(data, reverse=True))

# === Stack Operations (use list as stack) ===
stack = []
stack.append(1)    # push
stack.append(2)
stack.append(3)
top = stack.pop()  # pop - O(1)
print("\nstack pop:", top, "remaining:", stack)

# === Shallow vs Deep Copy ===
import copy

nested = [[1, 2], [3, 4]]
shallow = nested[:]               # or nested.copy() or list(nested)
deep = copy.deepcopy(nested)

nested[0][0] = 999
print("\nshallow affected:", shallow[0][0])   # 999 - inner lists are shared
print("deep unaffected:", deep[0][0])         # 1

# === Common Interview Gotchas ===

# 1. Mutable default argument trap
# BAD: def func(lst=[]): ...  -> shared across calls
# GOOD: def func(lst=None): lst = lst if lst is not None else []

# 2. Creating 2D arrays
# BAD:  grid = [[0] * 3] * 3   -> all rows are the SAME object
# GOOD: grid = [[0] * 3 for _ in range(3)]

bad_grid = [[0] * 3] * 3
bad_grid[0][0] = 1
print("\nbad grid (all rows modified):", bad_grid)

good_grid = [[0] * 3 for _ in range(3)]
good_grid[0][0] = 1
print("good grid (only row 0):", good_grid)

# 3. Modifying a list while iterating
# BAD:  for x in lst: lst.remove(x)
# GOOD: lst = [x for x in lst if condition(x)]

# === Time Complexity Summary ===
# append:       O(1) amortized
# pop():        O(1)
# pop(i):       O(n)
# insert(i, x): O(n)
# remove(x):    O(n)
# x in list:    O(n)
# index(x):     O(n)
# sort():       O(n log n)
# len():        O(1)
# slice [a:b]:  O(b - a)
