"""
Python itertools - Iterator Building Blocks
=============================================
Efficient tools for working with iterables.
All return lazy iterators (memory efficient).
"""

import itertools

# ============================================================
# Infinite Iterators
# ============================================================
print("=== Infinite Iterators ===")

# count(start, step) - infinite counter
from itertools import islice
counter = itertools.count(10, 2)       # 10, 12, 14, 16, ...
print("count:", list(islice(counter, 5)))

# cycle(iterable) - repeat endlessly
cycler = itertools.cycle("ABC")
print("cycle:", [next(cycler) for _ in range(7)])  # A B C A B C A

# repeat(elem, n) - repeat element n times (or forever if n omitted)
print("repeat:", list(itertools.repeat("x", 4)))

# ============================================================
# Combinatoric Iterators
# ============================================================
print("\n=== Combinatorics ===")

# permutations(iterable, r) - ordered arrangements
print("permutations(ABC, 2):")
for p in itertools.permutations("ABC", 2):
    print(f"  {p}")
# ('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')
# n!/(n-r)! = 3!/1! = 6

# combinations(iterable, r) - unordered, no replacement
print("combinations(ABC, 2):")
for c in itertools.combinations("ABC", 2):
    print(f"  {c}")
# ('A','B'), ('A','C'), ('B','C')
# n!/(r!(n-r)!) = 3!/(2!*1!) = 3

# combinations_with_replacement(iterable, r)
print("combinations_with_replacement(AB, 2):")
for c in itertools.combinations_with_replacement("AB", 2):
    print(f"  {c}")
# ('A','A'), ('A','B'), ('B','B')

# product(iterables, repeat) - cartesian product
print("product(01, repeat=2):")
for p in itertools.product("01", repeat=2):
    print(f"  {p}")
# ('0','0'), ('0','1'), ('1','0'), ('1','1')

# Cartesian product of multiple iterables
print("product([1,2], ['a','b']):")
for p in itertools.product([1, 2], ["a", "b"]):
    print(f"  {p}")

# ============================================================
# Terminating Iterators
# ============================================================
print("\n=== Terminating Iterators ===")

# chain(*iterables) - concatenate iterables
chained = itertools.chain([1, 2], [3, 4], [5])
print("chain:", list(chained))         # [1, 2, 3, 4, 5]

# chain.from_iterable - flatten one level
nested = [[1, 2], [3, 4], [5]]
flat = list(itertools.chain.from_iterable(nested))
print("flatten:", flat)

# islice(iterable, stop) or islice(iterable, start, stop, step)
print("islice:", list(itertools.islice(range(100), 2, 10, 3)))  # [2, 5, 8]

# compress(data, selectors) - filter by mask
data = "ABCDEF"
mask = [1, 0, 1, 0, 1, 1]
print("compress:", list(itertools.compress(data, mask)))  # A C E F

# takewhile / dropwhile
nums = [1, 3, 5, 2, 4, 6]
print("takewhile <5:", list(itertools.takewhile(lambda x: x < 5, nums)))  # [1, 3]
print("dropwhile <5:", list(itertools.dropwhile(lambda x: x < 5, nums)))  # [5, 2, 4, 6]

# accumulate(iterable, func) - running totals
nums = [1, 2, 3, 4, 5]
print("accumulate sum:", list(itertools.accumulate(nums)))           # [1, 3, 6, 10, 15]
print("accumulate max:", list(itertools.accumulate(nums, max)))      # [1, 2, 3, 4, 5]
print("accumulate mul:", list(itertools.accumulate(nums, lambda a, b: a * b)))

# starmap(func, iterable) - apply func to unpacked arguments
pairs = [(2, 3), (4, 5), (6, 7)]
print("starmap pow:", list(itertools.starmap(pow, pairs)))  # [8, 1024, 279936]

# ============================================================
# groupby
# ============================================================
print("\n=== groupby ===")

# IMPORTANT: data must be sorted by the grouping key first!
data = [("fruit", "apple"), ("fruit", "banana"),
        ("veggie", "carrot"), ("veggie", "pea")]

for key, group in itertools.groupby(data, key=lambda x: x[0]):
    items = [item[1] for item in group]
    print(f"  {key}: {items}")

# Group consecutive equal elements
s = "AAABBBCCAAB"
for key, group in itertools.groupby(s):
    print(f"  {key}: {list(group)}")

# ============================================================
# zip_longest
# ============================================================
print("\n=== zip_longest ===")

# Regular zip stops at shortest
print("zip:", list(zip([1, 2, 3], ["a", "b"])))  # [(1,'a'), (2,'b')]

# zip_longest pads with fillvalue
zipped = itertools.zip_longest([1, 2, 3], ["a", "b"], fillvalue="-")
print("zip_longest:", list(zipped))    # [(1,'a'), (2,'b'), (3,'-')]

# ============================================================
# Common Interview Patterns
# ============================================================
print("\n=== Interview Patterns ===")

# 1. Generate all subsets (power set)
def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )

print("powerset(ABC):", list(powerset("ABC")))

# 2. Sliding window (fixed size)
def sliding_window(iterable, n):
    it = iter(iterable)
    window = list(islice(it, n))
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window = window[1:] + [x]
        yield tuple(window)

print("sliding window:", list(sliding_window([1, 2, 3, 4, 5], 3)))

# 3. Pairwise iteration
def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

print("pairwise:", list(pairwise([1, 2, 3, 4])))  # [(1,2), (2,3), (3,4)]
# Note: itertools.pairwise() exists in Python 3.10+

# 4. Flatten nested iterables
nested = [[1, 2], [3], [4, 5, 6]]
print("flattened:", list(itertools.chain.from_iterable(nested)))

# 5. All pairs from two lists
list1 = [1, 2]
list2 = ["a", "b", "c"]
print("all pairs:", list(itertools.product(list1, list2)))

# === Tips ===
# 1. itertools returns lazy iterators -- memory efficient
# 2. combinations for "choose k from n" problems
# 3. product for brute-force exploration of search spaces
# 4. accumulate for prefix sums
# 5. groupby requires sorted input (or consecutive groups)
# 6. chain.from_iterable for flattening one level
