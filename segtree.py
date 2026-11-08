from math import ceil

from python.heap import Binheap
from collections.abc import Callable

# TODO: fix this
def segtree_minhimplementation(operation: Callable[[float, float], float]):
    """
    # this is a segtree operating on float/integer values.
    input:
        operation(x, y) -> z
            satisfy 
                if a<b<c:
                    operation(info(a, b), info(b, c)) = info(a,c)
                example:
                    operation = lambda x, y: x + y
                    info(a, b) = sum of elements in range [a, b]

    info(l, r) represent the information stored in the segment tree node covering the range [l, r].

    update(l, r, i, v) is a function to update tree given the new the i value.

    the segtree support range queries:
        info(l, r) in O(log n)
        update(l, r, new_info(l,r)) in O(log n)
    """
    data: list[float] = []
    grand_border = -1 #TODO

    def get_parent_index(i):
        return (i - 1) // 2

    def get_left_child_index(i):
        return 2 * i + 1

    def get_right_child_index(i):
        return 2 * i + 2


    def info(l, r):
        left_index = 0 #index of the left border segment
        search_left, search_right = 0, len(data)
        while left_index < len(data):
            border = ceil((search_left + search_right) / 2)
            if l == border:
                left_index = get_right_child_index(left_index)
                break
            elif left_index < border:
                search_right = border
                left_index = get_right_child_index(left_index)
            else:
                search_left = border
                left_index = get_left_child_index(left_index)
        # left_index is now the index of the segment covering the left border of the range [l, r]
        right_index = 0 #index of the right border segment
        search_left, search_right = 0, len(data)
        while right_index < len(data):
            border = ceil((search_left + search_right) / 2)
            if r == border:
                right_index = get_right_child_index(right_index)
                break
            elif right_index < border:
                search_left = border
                right_index = get_left_child_index(right_index)
            else:
                search_right = border
                right_index = get_right_child_index(right_index)
        # right_index is now the index of the segment covering the right border of the range [l, r]
        return operation(data[left_index], data[right_index])

    def get_index_of(i):
        pass

    def update(l, r, i, v):
        node_index = 0
        while node_index < len(data):

        data[node_index] = v

    return info, update