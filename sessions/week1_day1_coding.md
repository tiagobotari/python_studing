# Week 1 - Day 1: Coding Practice (2 hours)
## Focus: Python warm-up + arrays/hash maps + intro to graph problems

---

## Block 1: Python Warm-Up (30 min) - 3 Easy problems

### Problem 1: [Two Sum (LeetCode #1)](https://leetcode.com/problems/two-sum/)
**Difficulty:** Easy | **Topic:** Hash Maps | **Target:** 10 min
**Code:** [solution.py](week1_day1/p1_two_sum/solution.py) | **Tests:** [test_solution.py](week1_day1/p1_two_sum/test_solution.py) | `cd week1_day1/p1_two_sum && pytest`

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution, and you may not use the same element twice.

```
Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]   # because nums[0] + nums[1] = 9
```

**Try it yourself first, then check the solution below.**

<details>
<summary>Hint 1</summary>

Brute force: O(n^2) with two nested loops
</details>

<details>
<summary>Hint 2</summary>

Optimal: use a hash map to store seen values -> O(n)
</details>

<details>
<summary>Hint 3</summary>

For each number, check if `target - num` is already in the map
</details>

<details>
<summary>Solution</summary>

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Time: O(n), Space: O(n)
```

**Key takeaway:** Hash maps turn O(n^2) lookups into O(n). This pattern appears constantly.
</details>

---

### Problem 2: [Valid Anagram (LeetCode #242)](https://leetcode.com/problems/valid-anagram/)
**Difficulty:** Easy | **Topic:** Hash Maps / Counting | **Target:** 10 min
**Code:** [solution.py](week1_day1/p2_valid_anagram/solution.py) | **Tests:** [test_solution.py](week1_day1/p2_valid_anagram/test_solution.py) | `cd week1_day1/p2_valid_anagram && pytest`

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

```
Example:
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False
```

<details>
<summary>Hint 1</summary>

Count character frequencies in both strings
</details>

<details>
<summary>Hint 2</summary>

Python's `collections.Counter` makes this trivial
</details>

<details>
<summary>Hint 3</summary>

Or use a single dict: increment for s, decrement for t
</details>

<details>
<summary>Solution</summary>

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Or without Counter:
def is_anagram_manual(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in t:
        counts[c] = counts.get(c, 0) - 1
        if counts[c] < 0:
            return False
    return True

# Time: O(n), Space: O(1) since alphabet is fixed
```

**Key takeaway:** Character counting with dicts/Counter is a fundamental pattern.
</details>

---

### Problem 3: [Contains Duplicate (LeetCode #217)](https://leetcode.com/problems/contains-duplicate/)
**Difficulty:** Easy | **Topic:** Hash Sets | **Target:** 5 min
**Code:** [solution.py](week1_day1/p3_contains_duplicate/solution.py) | **Tests:** [test_solution.py](week1_day1/p3_contains_duplicate/test_solution.py) | `cd week1_day1/p3_contains_duplicate && pytest`

Given an integer array `nums`, return `True` if any value appears at least twice, and `False` if every element is distinct.

```
Example:
Input: nums = [1, 2, 3, 1]
Output: True
```

<details>
<summary>Solution</summary>

```python
def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# Or explicitly:
def contains_duplicate_v2(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Time: O(n), Space: O(n)
```

**Key takeaway:** Sets give O(1) membership testing. Early return in v2 is faster on average.
</details>

---

## Block 2: Array Patterns (40 min) - 3 Easy/Medium problems

### Problem 4: [Best Time to Buy and Sell Stock (LeetCode #121)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
**Difficulty:** Easy | **Topic:** Arrays, Sliding Window | **Target:** 15 min
**Code:** [solution.py](week1_day1/p4_buy_sell_stock/solution.py) | **Tests:** [test_solution.py](week1_day1/p4_buy_sell_stock/test_solution.py) | `cd week1_day1/p4_buy_sell_stock && pytest`

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit from one buy-sell transaction. Return 0 if no profit is possible.

```
Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5   # Buy on day 1 (price=1), sell on day 4 (price=6)
```

<details>
<summary>Hint 1</summary>

Track the minimum price seen so far
</details>

<details>
<summary>Hint 2</summary>

At each step, compute profit = current_price - min_price_so_far
</details>

<details>
<summary>Hint 3</summary>

Keep track of the maximum profit
</details>

<details>
<summary>Solution</summary>

```python
def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# Time: O(n), Space: O(1)
```

**Key takeaway:** "Track the best so far" is a core pattern. Single-pass with running min/max.
</details>

---

### Problem 5: [Product of Array Except Self (LeetCode #238)](https://leetcode.com/problems/product-of-array-except-self/)
**Difficulty:** Medium | **Topic:** Arrays, Prefix | **Target:** 15 min
**Code:** [solution.py](week1_day1/p5_product_except_self/solution.py) | **Tests:** [test_solution.py](week1_day1/p5_product_except_self/test_solution.py) | `cd week1_day1/p5_product_except_self && pytest`

Given an integer array `nums`, return an array `answer` such that `answer[i]` is the product of all elements except `nums[i]`. You must solve it without using division and in O(n) time.

```
Example:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

<details>
<summary>Hint 1</summary>

Think prefix and suffix products
</details>

<details>
<summary>Hint 2</summary>

answer[i] = (product of everything left of i) * (product of everything right of i)
</details>

<details>
<summary>Hint 3</summary>

Two passes: left-to-right for prefix, right-to-left for suffix
</details>

<details>
<summary>Solution</summary>

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # Left pass: answer[i] = product of nums[0..i-1]
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Right pass: multiply by product of nums[i+1..n-1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

# Time: O(n), Space: O(1) extra (output array doesn't count)
```

**Key takeaway:** Prefix/suffix decomposition. This "two-pass" trick appears in many problems.
</details>

---

### Problem 6: [Group Anagrams (LeetCode #49)](https://leetcode.com/problems/group-anagrams/)
**Difficulty:** Medium | **Topic:** Hash Maps, Sorting | **Target:** 10 min
**Code:** [solution.py](week1_day1/p6_group_anagrams/solution.py) | **Tests:** [test_solution.py](week1_day1/p6_group_anagrams/test_solution.py) | `cd week1_day1/p6_group_anagrams && pytest`

Given an array of strings `strs`, group the anagrams together. Return the answer in any order.

```
Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

<details>
<summary>Hint 1</summary>

Anagrams have the same sorted characters
</details>

<details>
<summary>Hint 2</summary>

Use sorted string as a hash map key
</details>

<details>
<summary>Hint 3</summary>

Or use a tuple of character counts as the key
</details>

<details>
<summary>Solution</summary>

```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# Time: O(n * k log k) where k is max string length
# Space: O(n * k)
```

**Key takeaway:** Transforming data into a canonical form (sorted string) to use as a hash key.
</details>

---

## Block 3: Graph Fundamentals (50 min) - 3 problems

These are directly relevant to your GNN work: graph traversal is the algorithmic backbone of message passing.

### Problem 7: [Number of Islands (LeetCode #200)](https://leetcode.com/problems/number-of-islands/)
**Difficulty:** Medium | **Topic:** BFS/DFS on Grid | **Target:** 15 min
**Code:** [solution.py](week1_day1/p7_number_of_islands/solution.py) | **Tests:** [test_solution.py](week1_day1/p7_number_of_islands/test_solution.py) | `cd week1_day1/p7_number_of_islands && pytest`

Given a 2D grid of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

```
Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

<details>
<summary>Hint 1</summary>

Iterate through the grid; when you find a '1', that's a new island
</details>

<details>
<summary>Hint 2</summary>

Use DFS/BFS to mark all connected '1's as visited
</details>

<details>
<summary>Hint 3</summary>

Count how many times you start a new DFS/BFS
</details>

<details>
<summary>Solution</summary>

```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count

# Time: O(rows * cols), Space: O(rows * cols) worst case recursion
```

**Key takeaway:** Grid DFS is the 2D version of graph traversal. This "flood fill" pattern is fundamental. Think of it as message passing on a grid graph with 4-connectivity.
</details>

---

### Problem 8: [Clone Graph (LeetCode #133)](https://leetcode.com/problems/clone-graph/)
**Difficulty:** Medium | **Topic:** Graph DFS/BFS, Hash Map | **Target:** 20 min
**Code:** [solution.py](week1_day1/p8_clone_graph/solution.py) | **Tests:** [test_solution.py](week1_day1/p8_clone_graph/test_solution.py) | `cd week1_day1/p8_clone_graph && pytest`

Given a reference to a node in a connected undirected graph, return a deep copy of the graph. Each node has a value and a list of neighbors.

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

<details>
<summary>Hint 1</summary>

Use a hash map: old_node -> cloned_node
</details>

<details>
<summary>Hint 2</summary>

DFS/BFS through the original graph
</details>

<details>
<summary>Hint 3</summary>

For each node, create a clone if not already created, then recursively clone neighbors
</details>

<details>
<summary>Solution</summary>

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Node) -> Node:
    if not node:
        return None

    cloned = {}

    def dfs(n):
        if n in cloned:
            return cloned[n]
        copy = Node(n.val)
        cloned[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)

# Time: O(V + E), Space: O(V)
```

**Key takeaway:** The old->new hash map pattern for graph cloning. This is analogous to how GNN frameworks manage computational graphs - each node maintains references to its neighbors.
</details>

---

### Problem 9: [Course Schedule (LeetCode #207)](https://leetcode.com/problems/course-schedule/)
**Difficulty:** Medium | **Topic:** Topological Sort, Cycle Detection | **Target:** 15 min
**Code:** [solution.py](week1_day1/p9_course_schedule/solution.py) | **Tests:** [test_solution.py](week1_day1/p9_course_schedule/test_solution.py) | `cd week1_day1/p9_course_schedule && pytest`

There are `numCourses` courses (0 to numCourses-1). You are given prerequisite pairs where `[a, b]` means you must take course `b` before `a`. Return `True` if you can finish all courses (i.e., no circular dependency).

```
Example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: True   # Take course 0, then course 1

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False  # Circular dependency
```

<details>
<summary>Hint 1</summary>

Build an adjacency list from prerequisites
</details>

<details>
<summary>Hint 2</summary>

This is a cycle detection problem on a directed graph
</details>

<details>
<summary>Hint 3</summary>

Use DFS with 3 states: unvisited, in-progress, visited
</details>

<details>
<summary>Hint 4</summary>

If you visit an in-progress node, there's a cycle
</details>

<details>
<summary>Solution</summary>

```python
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # Build adjacency list
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0 = unvisited, 1 = in-progress, 2 = visited
    state = [0] * num_courses

    def has_cycle(node):
        if state[node] == 1:  # cycle detected
            return True
        if state[node] == 2:  # already fully explored
            return False
        state[node] = 1
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = 2
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False
    return True

# Time: O(V + E), Space: O(V + E)
```

**Key takeaway:** Topological sort / cycle detection on directed graphs. The 3-state DFS pattern (unvisited, in-progress, done) is essential for directed graph problems.
</details>

---

## Session Debrief (last 5 min)

### Patterns practiced today:
1. **Hash map for O(1) lookup** - Two Sum, Group Anagrams
2. **Counting / frequency maps** - Anagram, Contains Duplicate
3. **Single-pass with running state** - Buy/Sell Stock
4. **Prefix/suffix decomposition** - Product of Array Except Self
5. **Grid DFS (flood fill)** - Number of Islands
6. **Graph DFS with hash map** - Clone Graph
7. **Cycle detection (3-state DFS)** - Course Schedule

### For tomorrow:
- Review any problems you struggled with
- Try solving them again without looking at solutions
- Next session: more graph problems (BFS, shortest path, connected components)

### Track your progress:
- [ ] Problem 1: Two Sum
- [ ] Problem 2: Valid Anagram
- [ ] Problem 3: Contains Duplicate
- [ ] Problem 4: Best Time to Buy and Sell Stock
- [ ] Problem 5: Product of Array Except Self
- [ ] Problem 6: Group Anagrams
- [ ] Problem 7: Number of Islands
- [ ] Problem 8: Clone Graph
- [ ] Problem 9: Course Schedule
