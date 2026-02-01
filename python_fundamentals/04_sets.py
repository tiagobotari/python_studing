"""
Python Sets - Hash Sets
========================
- Unordered collection of unique, hashable elements
- Average O(1) membership testing, insert, delete
- Supports mathematical set operations
"""

# === Creation ===
empty = set()                          # NOT {} -- that's an empty dict!
from_literal = {1, 2, 3}
from_list = set([1, 2, 2, 3, 3])      # duplicates removed -> {1, 2, 3}
from_string = set("hello")            # {'h', 'e', 'l', 'o'}

print("from_list:", from_list)
print("from_string:", from_string)

# === Add / Remove ===
s = {1, 2, 3}
s.add(4)                              # O(1)
s.add(2)                              # no effect, already present
s.remove(1)                           # O(1) - raises KeyError if missing
s.discard(99)                         # O(1) - safe, no error if missing
popped = s.pop()                      # removes arbitrary element
print("\nafter operations:", s, "popped:", popped)

# === Membership Testing ===
s = {10, 20, 30, 40, 50}
print("\n20 in s:", 20 in s)           # O(1) average -- this is why sets exist
print("99 in s:", 99 in s)            # O(1) average

# Compare: list membership is O(n), set membership is O(1)

# === Set Operations ===
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union: elements in a OR b
print("\nunion:", a | b)                # {1, 2, 3, 4, 5, 6}
print("union:", a.union(b))            # same

# Intersection: elements in a AND b
print("intersection:", a & b)          # {3, 4}
print("intersection:", a.intersection(b))

# Difference: elements in a but NOT in b
print("difference:", a - b)            # {1, 2}
print("difference:", a.difference(b))

# Symmetric difference: elements in a XOR b (in one but not both)
print("symmetric diff:", a ^ b)        # {1, 2, 5, 6}
print("symmetric diff:", a.symmetric_difference(b))

# === In-Place Set Operations ===
a = {1, 2, 3, 4}
a |= {5, 6}           # a.update({5, 6})
print("\nafter |=:", a)
a &= {2, 4, 6}        # a.intersection_update({2, 4, 6})
print("after &=:", a)
a -= {2}               # a.difference_update({2})
print("after -=:", a)

# === Subset / Superset ===
small = {1, 2}
big = {1, 2, 3, 4}

print("\nsubset:", small <= big)        # True - small is subset of big
print("proper subset:", small < big)   # True - subset and not equal
print("superset:", big >= small)       # True
print("disjoint:", {1, 2}.isdisjoint({3, 4}))  # True - no common elements

# === Frozenset (immutable set) ===
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError - can't modify

# Frozensets can be dict keys or set members
sets_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print("\nset of frozensets:", sets_of_sets)

# === Common Interview Patterns ===

# 1. Remove duplicates while preserving order
def unique_ordered(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

print("\nunique ordered:", unique_ordered([3, 1, 4, 1, 5, 3]))

# 2. Find duplicates
def find_duplicates(lst):
    seen = set()
    dupes = set()
    for x in lst:
        if x in seen:
            dupes.add(x)
        seen.add(x)
    return dupes

print("duplicates:", find_duplicates([1, 2, 3, 2, 4, 3]))

# 3. Two-set intersection (e.g., common elements)
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("common:", common)

# === Time Complexity Summary ===
# add(x):       O(1) average
# remove(x):    O(1) average
# discard(x):   O(1) average
# x in set:     O(1) average  <-- the key advantage
# len():        O(1)
# union:        O(len(a) + len(b))
# intersection: O(min(len(a), len(b)))
# difference:   O(len(a))

# === Interview Tips ===
# 1. Use set for O(1) membership testing -- the #1 reason to use sets
# 2. set() removes duplicates but loses order
# 3. frozenset for when you need a hashable set (dict key, nested set)
# 4. Set operations are cleaner than manual loops for overlap problems
# 5. {} is an empty DICT, not an empty set -- use set() for empty sets
