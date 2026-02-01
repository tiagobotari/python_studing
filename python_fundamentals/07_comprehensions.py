"""
Python Comprehensions & Generators
====================================
- Concise syntax for creating lists, dicts, sets
- Generator expressions for lazy evaluation
- Often faster than equivalent for-loops
"""

# ============================================================
# List Comprehensions
# ============================================================
print("=== List Comprehensions ===")

# Basic: [expression for item in iterable]
squares = [x**2 for x in range(6)]
print("squares:", squares)

# With filter: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print("evens:", evens)

# With transform + filter
big_squares = [x**2 for x in range(10) if x**2 > 20]
print("big squares:", big_squares)

# Ternary inside comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print("labels:", labels)

# Nested loops (flatten)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print("flattened:", flat)
# Equivalent to:
# for row in matrix:
#     for x in row:
#         flat.append(x)

# 2D creation
grid = [[0] * 3 for _ in range(3)]     # 3x3 grid of zeros
print("grid:", grid)

# ============================================================
# Dict Comprehensions
# ============================================================
print("\n=== Dict Comprehensions ===")

# Basic: {key_expr: val_expr for item in iterable}
sq_dict = {x: x**2 for x in range(6)}
print("squares dict:", sq_dict)

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print("inverted:", inverted)

# With filter
even_sq = {x: x**2 for x in range(10) if x % 2 == 0}
print("even squares:", even_sq)

# Word frequency
words = ["hello", "world", "hello", "python"]
freq = {w: words.count(w) for w in set(words)}
print("freq:", freq)

# ============================================================
# Set Comprehensions
# ============================================================
print("\n=== Set Comprehensions ===")

# Basic: {expression for item in iterable}
unique_lengths = {len(w) for w in ["hello", "hi", "hey", "world"]}
print("unique lengths:", unique_lengths)

# First letters
first_chars = {w[0] for w in ["apple", "banana", "avocado", "cherry"]}
print("first chars:", first_chars)

# ============================================================
# Generator Expressions (lazy comprehensions)
# ============================================================
print("\n=== Generator Expressions ===")

# Use () instead of [] -- produces values lazily (one at a time)
gen = (x**2 for x in range(5))
print("generator:", gen)               # generator object, not a list
print("list(gen):", list(gen))         # consume into list
# print("list(gen):", list(gen))       # empty! generators are one-shot

# Memory efficient: doesn't create entire list in memory
total = sum(x**2 for x in range(1000000))  # no list created
print("sum of squares:", total)

# Useful with any(), all()
nums = [2, 4, 6, 8]
print("\nall even:", all(x % 2 == 0 for x in nums))    # True
print("any > 5:", any(x > 5 for x in nums))            # True

# Find first match
names = ["Alice", "Bob", "Charlie", "Diana"]
first_long = next((n for n in names if len(n) > 5), None)
print("first long name:", first_long)   # Charlie

# ============================================================
# Generator Functions (yield)
# ============================================================
print("\n=== Generator Functions ===")

def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("fibonacci:", list(fibonacci(10)))

# Infinite generator
def count_from(start=0):
    n = start
    while True:
        yield n
        n += 1

# Take first 5 from infinite generator
from itertools import islice
print("count from 10:", list(islice(count_from(10), 5)))

# Generator pipeline (chaining)
def evens(iterable):
    for x in iterable:
        if x % 2 == 0:
            yield x

def squared(iterable):
    for x in iterable:
        yield x ** 2

# Compose: squared even numbers from 0-9
pipeline = squared(evens(range(10)))
print("pipeline:", list(pipeline))     # [0, 4, 16, 36, 64]

# ============================================================
# Walrus Operator in Comprehensions (Python 3.8+)
# ============================================================
print("\n=== Walrus Operator ===")

# Avoid computing expression twice
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [y for x in data if (y := x**2) > 20]
print("squares > 20:", results)

# ============================================================
# Common Interview Patterns
# ============================================================
print("\n=== Interview Patterns ===")

# 1. Transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [list(row) for row in zip(*matrix)]
print("transposed:", transposed)

# 2. Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flat = [x for sublist in nested for x in sublist]
print("flat:", flat)

# 3. Character frequency with dict comprehension
s = "abracadabra"
freq = {ch: s.count(ch) for ch in set(s)}
print("freq:", freq)

# 4. Filter and transform in one pass
nums = range(20)
result = [x**2 for x in nums if x % 3 == 0 and x > 0]
print("multiples of 3 squared:", result)

# === Tips ===
# 1. List comp is ~30% faster than equivalent for-loop with append
# 2. Use generator expressions when you only need to iterate once
# 3. Generators are memory-efficient for large/infinite sequences
# 4. Don't nest more than 2 levels deep -- use a regular loop instead
# 5. Comprehensions create a new scope (variables don't leak in Python 3)
