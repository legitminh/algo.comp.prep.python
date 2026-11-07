from collections.abc import Sequence

from collections import deque

def maxflow(n, edges, s, t):
    from dinichmaxflow import Graph
    g = Graph(n)
    for u, v, c in edges:
        g.addEdge(u, v, c)

    return g.DinicMaxflow(s, t)


edges = [
    (0, 1, 1),  # S -> A
    (0, 2, 1),  # S -> B
    (1, 2, 1),  # A -> B
    (1, 3, 1),  # A -> T
    (2, 3, 1),  # B -> T
]

print(maxflow(4, edges, 0, 3))  # 2

