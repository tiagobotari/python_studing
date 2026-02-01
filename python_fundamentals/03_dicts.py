"""
Python Dicts - Hash Maps
=========================
- Ordered (insertion order guaranteed since Python 3.7)
- Mutable mapping of hashable keys to arbitrary values
- Average O(1) lookup, insert, delete
"""

# === Creation ===
empty = {}
from_literal = {"a": 1, "b": 2}
from_constructor = dict(a=1, b=2)
from_pairs = dict([("a", 1), ("b", 2)])
from_zip = dict(zip(["a", "b"], [1, 2]))
from_comprehension = {x: x**2 for x in range(5)}

print("from_zip:", from_zip)
print("from_comprehension:", from_comprehension)

# === Access ===
d = {"name": "Alice", "age": 30}

print("\nd['name']:", d["name"])
# d["missing"]  # KeyError!

# Safe access with .get()
print("get missing:", d.get("missing"))          # None
print("get with default:", d.get("missing", 0))  # 0

# === Insert / Update ===
d["email"] = "alice@example.com"    # O(1)
d["age"] = 31                        # update existing key
d.update({"age": 32, "city": "NYC"}) # batch update

print("\nupdated:", d)

# Merge dicts (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2                     # d2 values win on conflict
print("merged:", merged)             # {'a': 1, 'b': 3, 'c': 4}

# === Delete ===
d = {"a": 1, "b": 2, "c": 3}
del d["a"]                           # O(1) - KeyError if missing
val = d.pop("b")                     # O(1) - returns value, KeyError if missing
val2 = d.pop("missing", None)        # safe pop with default
print("\nafter delete:", d, "popped:", val)

# === Iteration ===
d = {"x": 10, "y": 20, "z": 30}

print("\nkeys:")
for k in d:                          # iterates over keys by default
    print(f"  {k}")

print("values:")
for v in d.values():
    print(f"  {v}")

print("items:")
for k, v in d.items():               # most common pattern
    print(f"  {k}: {v}")

# === Useful Methods ===
d = {"a": 1, "b": 2}

# setdefault: get value or set it if missing
val = d.setdefault("c", 0)          # sets d["c"] = 0, returns 0
print("\nsetdefault:", d)

# keys, values, items return view objects (live views)
keys = d.keys()
d["d"] = 4
print("keys view updated:", list(keys))  # includes 'd'

# === Counting Pattern (without Counter) ===
text = "abracadabra"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("\nfrequency:", freq)

# === Grouping Pattern ===
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}
for w in words:
    key = tuple(sorted(w))
    groups.setdefault(key, []).append(w)
print("groups:", list(groups.values()))

# === Dictionary Ordering ===
# Insertion order is preserved (Python 3.7+)
d = {}
d["first"] = 1
d["second"] = 2
d["third"] = 3
print("\nordered keys:", list(d.keys()))  # ['first', 'second', 'third']

# popitem() removes the LAST inserted item (LIFO)
last = d.popitem()
print("popitem:", last)  # ('third', 3)

# === What Can Be a Key? ===
# Keys must be hashable: int, float, str, tuple, frozenset, bool, None
valid = {
    42: "int",
    "key": "str",
    (1, 2): "tuple",
    frozenset([1, 2]): "frozenset",
    True: "bool",
    None: "none",
}
print("\nvalid keys:", list(valid.keys()))

# Lists, dicts, sets are NOT hashable -> can't be keys
# {[1, 2]: "bad"}  # TypeError: unhashable type: 'list'

# === Time Complexity Summary ===
# d[key]:          O(1) average
# d[key] = val:    O(1) average
# del d[key]:      O(1) average
# key in d:        O(1) average
# d.get(key):      O(1) average
# len(d):          O(1)
# d.items():       O(1) to create view, O(n) to iterate
# d.copy():        O(n) shallow copy

# === Interview Tips ===
# 1. dict is the go-to for O(1) lookup -- "hash map" in interview speak
# 2. Use .get() to avoid KeyError, setdefault() to init-and-get
# 3. Counting and grouping are the two most common dict patterns
# 4. Keys must be hashable: use tuple instead of list for composite keys
# 5. Worst-case O(n) for hash collisions, but almost never in practice
