"""
Python collections Module - Specialized Containers
====================================================
Key types: Counter, defaultdict, deque, OrderedDict, namedtuple
These are the most interview-relevant extensions to built-in types.
"""

from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

# ============================================================
# Counter - Count hashable objects
# ============================================================
print("=== Counter ===")

# Creation
c = Counter("abracadabra")
print("from string:", c)               # Counter({'a': 5, 'b': 2, 'r': 2, ...})

c2 = Counter([1, 1, 2, 3, 3, 3])
print("from list:", c2)

# Access
print("\ncount of 'a':", c["a"])        # 5
print("missing key:", c["z"])           # 0 (no KeyError!)

# Most common
print("most common 2:", c.most_common(2))  # [('a', 5), ('b', 2)]

# Arithmetic
c1 = Counter("aab")
c2 = Counter("abc")
print("\nc1 + c2:", c1 + c2)            # add counts
print("c1 - c2:", c1 - c2)             # subtract (drops zero/negative)
print("c1 & c2:", c1 & c2)             # min of each count (intersection)
print("c1 | c2:", c1 | c2)             # max of each count (union)

# Total count
print("total:", c1.total())             # sum of all counts

# Iterate over elements (repeats by count)
print("elements:", list(c1.elements()))  # ['a', 'a', 'b']

# ============================================================
# defaultdict - Dict with default factory
# ============================================================
print("\n=== defaultdict ===")

# Grouping pattern (most common use)
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for w in words:
    key = tuple(sorted(w))
    groups[key].append(w)
print("groups:", dict(groups))

# Counting pattern
counts = defaultdict(int)
for ch in "abracadabra":
    counts[ch] += 1                    # missing key auto-initializes to 0
print("counts:", dict(counts))

# Set of sets
graph = defaultdict(set)
edges = [(1, 2), (1, 3), (2, 3)]
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)
print("graph:", dict(graph))

# Nested defaultdict
tree = lambda: defaultdict(tree)
taxonomy = tree()
taxonomy["animal"]["mammal"]["dog"] = True
print("nested:", taxonomy["animal"]["mammal"]["dog"])

# ============================================================
# deque - Double-ended queue
# ============================================================
print("\n=== deque ===")

# Creation
d = deque([1, 2, 3])
print("deque:", d)

# Both ends are O(1)
d.append(4)            # O(1) - add to right
d.appendleft(0)        # O(1) - add to left
print("after appends:", d)

right = d.pop()        # O(1) - remove from right
left = d.popleft()     # O(1) - remove from left
print("popped:", left, right, "remaining:", d)

# Extend both ends
d.extend([4, 5])       # O(k)
d.extendleft([-1, 0])  # O(k) - note: items reversed!
print("extended:", d)

# Rotation
d = deque([1, 2, 3, 4, 5])
d.rotate(2)            # rotate right by 2
print("rotate right 2:", d)   # deque([4, 5, 1, 2, 3])
d.rotate(-2)           # rotate left by 2
print("rotate left 2:", d)    # back to [1, 2, 3, 4, 5]

# Fixed-size deque (sliding window)
window = deque(maxlen=3)
for i in range(5):
    window.append(i)
    print(f"  window after append({i}):", list(window))
# Automatically drops oldest when full

# BFS pattern with deque
print("\nBFS example:")
graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
visited = set()
queue = deque([1])
visited.add(1)
while queue:
    node = queue.popleft()             # O(1) -- list.pop(0) would be O(n)
    print(f"  visited: {node}")
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# ============================================================
# OrderedDict - Dict that remembers insertion order
# ============================================================
print("\n=== OrderedDict ===")

# Since Python 3.7, regular dict preserves insertion order too.
# OrderedDict is still useful for:

# 1. move_to_end (useful for LRU cache)
od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")                   # move 'a' to end
print("move_to_end:", list(od.keys()))  # ['b', 'c', 'a']
od.move_to_end("c", last=False)        # move 'c' to front
print("move_to_front:", list(od.keys()))

# 2. popitem with last=False (pop oldest)
oldest = od.popitem(last=False)
print("pop oldest:", oldest)

# LRU Cache pattern (simplified)
class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict oldest

lru = LRU(2)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)  # evicts 'a'
print("\nLRU get 'a':", lru.get("a"))   # -1 (evicted)
print("LRU get 'b':", lru.get("b"))     # 2

# ============================================================
# namedtuple - Lightweight immutable class
# ============================================================
print("\n=== namedtuple ===")

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print("point:", p)
print("p.x:", p.x, "p[0]:", p[0])     # access by name or index
print("as dict:", p._asdict())

# Useful for readability with structured data
Edge = namedtuple("Edge", ["src", "dst", "weight"])
edges = [Edge(0, 1, 5), Edge(1, 2, 3)]
for e in edges:
    print(f"  {e.src} -> {e.dst} (weight={e.weight})")

# === Time Complexity Summary ===
# Counter:
#   most_common(k): O(n log k)
#   +/-/&/|:        O(n)
#
# defaultdict:
#   Same as dict -- O(1) average for get/set/delete
#
# deque:
#   append/pop (both ends): O(1)
#   index access d[i]:       O(n)  <-- NOT O(1) like list!
#   rotate(k):               O(k)
#
# OrderedDict:
#   Same as dict + move_to_end: O(1)
