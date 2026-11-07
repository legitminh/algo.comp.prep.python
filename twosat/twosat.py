"""
f = (x1 or y1) and (x2 and 2) or ... or (xn and yn).
"""
from collections.abc import Iterable, Sequence



def invert_bool_int(s: int) -> int:
    return -s


def two_sat_kosaraju_class(clauses: Iterable[Sequence[int]]) -> bool:
    """
    SCC (Strongly Connected Components)
    if one thing is true, all is true. they form a loop
    """
    from kosaraju.kosaraju_class import Graph

    clauses = list(clauses)
    variables = {abs(literal) for clause in clauses for literal in clause}
    if not variables:
        return True

    g = Graph()

    for clause in clauses:
        x, y = clause
        nx, ny = invert_bool_int(x), invert_bool_int(y)
        g.add_edge(nx, y)
        g.add_edge(ny, x)


    scc_map = g.kosaraju_scc_dict()
    for variable in variables:
        if scc_map[variable] == scc_map[-variable]:
            return False

    return True


def two_sat_kosaraju(clauses: Iterable[Sequence[int]]) -> bool:
    from kosaraju import kosaraju

    clauses = list(clauses)
    variables = {abs(literal) for clause in clauses for literal in clause}
    vertices = variables | {-v for v in variables}
    if not variables:
        return True

    g = {vertex: [] for vertex in vertices}
    for clause in clauses:
        x, y = clause
        nx, ny = invert_bool_int(x), invert_bool_int(y)
        g[nx].append(y)
        g[ny].append(x)


    scc_map: dict[int, int] = kosaraju(g, vertices)
    for variable in variables:
        if scc_map[variable] == scc_map[-variable]:
            return False

    return True
    # TODO: add ability to return the actual assignment of variables if the formula is satisfiable

def two_sat(clauses: Iterable[Sequence[int]]) -> bool:
    return two_sat_kosaraju(clauses)

if __name__ == "__main__":
    example = [
        [1, 2], #or clause
        [-1, 2],
        [-1, -2],
        [1, -3]
    ]
    print(two_sat(example))