"""
Problem 8: Clone Graph (LeetCode #133)
https://leetcode.com/problems/clone-graph/

Given a reference to a node in a connected undirected graph, return a
deep copy of the graph. Each node has a value and a list of neighbors.
"""


class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    pass  # TODO: implement your solution here
