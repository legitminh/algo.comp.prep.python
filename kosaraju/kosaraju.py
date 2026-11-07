def kosaraju(graph: dict[int, list[int]], vertices: set[int]) -> dict[int, int]:
    # DFS construction
    visited = set()
    finished_order: list[int] = []

    def dfs(vertex):
        nonlocal finished_order, visited
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        finished_order.append(vertex)

    for vertex in vertices:
        if vertex not in visited:
            dfs(vertex)

    #transpose construction
    def make_tranpose(graph: dict[int, list[int]]) -> dict[int, list[int]]:
        transpose = {vertex: [] for vertex in vertices}
        for vertex in vertices:
            for neighbor in graph[vertex]:
                transpose[neighbor].append(vertex)
        return transpose

    transpose = make_tranpose(graph)

    # DFS on the transpose graph
    visited.clear()
    component_id = 0
    components: dict[int, int] = {}

    def dfs_transpose(vertex):
        nonlocal component_id, visited
        visited.add(vertex)
        components[vertex] = component_id
        for neighbor in transpose[vertex]:
            if neighbor not in visited:
                dfs_transpose(neighbor)

    for vertex in reversed(finished_order):
        if vertex not in visited:
            dfs_transpose(vertex)
            component_id += 1

    return components
