from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices: set[int] = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def _dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.append(v)

    def _transpose(self):
        transposed_graph = Graph()
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def _fill_order(self, visited, stack):
        for i in self.vertices:
            if not visited[i]:
                self._dfs(i, visited, stack)

    def _dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited, component)

    def kosaraju_scc(self) -> list[list[int]]:
        stack = deque()
        visited : dict[int, bool] = {v: False for v in self.vertices}
        self._fill_order(visited, stack)

        transposed_graph = self._transpose()

        visited : dict[int, bool] = {v: False for v in self.vertices}
        scc_list = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed_graph._dfs_util(node, visited, component)
                scc_list.append(component)

        return scc_list

    def kosaraju_scc_dict(self) -> dict[int, int]:
        stack = deque()
        visited : dict[int, bool] = {v: False for v in self.vertices}

        self._fill_order(visited, stack)

        transposed_graph = self._transpose()

        visited : dict[int, bool] = {v: False for v in self.vertices}
        scc_dict: dict[int, int] = {}
        scc_id = 0

        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed_graph._dfs_util(node, visited, component)
                for node in component:
                    scc_dict[node] = scc_id
                scc_id += 1

        return scc_dict

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    sccs = g.kosaraju_scc()
    print("Strongly Connected Components:", sccs)

    scc_dict = g.kosaraju_scc_dict()
    print("Strongly Connected Components Dictionary:", scc_dict)