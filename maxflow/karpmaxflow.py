from collections import deque

def karpmaxflow(n, edges, s, t):
    if s == t:
        return 0

    adj = [[] for _ in range(n)]
    cap = {}

    for u, v, c in edges:
        if (u, v) not in cap:
            adj[u].append(v)
            adj[v].append(u)
            cap[u, v] = 0
            cap[v, u] = 0

        cap[u, v] += c

    flow = 0

    while True:
        parent = [-1] * n
        parent[s] = s
        q = deque([s])

        # Find an augmenting path with BFS
        while q and parent[t] == -1:
            u = q.popleft()

            for v in adj[u]:
                if parent[v] == -1 and cap[u, v] > 0:
                    parent[v] = u
                    q.append(v)

        # No augmenting path -> maximum flow
        if parent[t] == -1:
            break

        # Find the bottleneck
        delta = float("inf")
        v = t

        while v != s:
            u = parent[v]
            delta = min(delta, cap[u, v])
            v = u

        # Update the residual graph
        v = t

        while v != s:
            u = parent[v]
            cap[u, v] -= delta
            cap[v, u] += delta
            v = u

        flow += delta

    return flow