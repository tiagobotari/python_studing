from solution import Node, clone_graph


def _build_graph(adj_list: list[list[int]]) -> Node | None:
    """Build a graph from an adjacency list (1-indexed)."""
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def _graph_to_adj(node: Node | None) -> dict[int, list[int]]:
    """Convert graph to adjacency dict for comparison."""
    if not node:
        return {}
    visited = {}
    stack = [node]
    while stack:
        n = stack.pop()
        if n.val in visited:
            continue
        visited[n.val] = sorted(nb.val for nb in n.neighbors)
        for nb in n.neighbors:
            if nb.val not in visited:
                stack.append(nb)
    return visited


def _collect_nodes(node: Node | None) -> set:
    """Collect all node object ids."""
    if not node:
        return set()
    visited = set()
    stack = [node]
    while stack:
        n = stack.pop()
        if id(n) in visited:
            continue
        visited.add(id(n))
        for nb in n.neighbors:
            stack.append(nb)
    return visited


def test_four_node_graph():
    # Graph: 1--2, 1--4, 2--3, 3--4
    original = _build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = clone_graph(original)

    # Structure must match
    assert _graph_to_adj(cloned) == _graph_to_adj(original)
    # Must be a deep copy (no shared node objects)
    assert _collect_nodes(original).isdisjoint(_collect_nodes(cloned))


def test_single_node():
    original = Node(1)
    cloned = clone_graph(original)

    assert cloned is not original
    assert cloned.val == 1
    assert cloned.neighbors == []


def test_none():
    assert clone_graph(None) is None


def test_two_nodes():
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]

    cloned = clone_graph(n1)
    assert cloned is not n1
    assert cloned.val == 1
    assert len(cloned.neighbors) == 1
    assert cloned.neighbors[0].val == 2
    assert cloned.neighbors[0] is not n2
