from collections.abc import Callable, Sequence
from operator import add
from typing import Literal


class SegmentTree:
    def __init__(
        self,
        arr: Sequence[int],
        operation: Literal["sum", "min"] = "sum",
    ) -> None:
        if not arr:
            raise ValueError("SegmentTree requires at least one value")
        if operation not in ("sum", "min"):
            raise ValueError(f"Unsupported operation: {operation}")

        self.n = len(arr)
        self.arr = list(arr)
        self._combine: Callable[[int, int], int] = add if operation == "sum" else min
        self.tree = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1)

    def _build(self, node_idx: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node_idx] = self.arr[start]
            return
        mid = (start + end) // 2
        self._build(2 * node_idx + 1, start, mid)
        self._build(2 * node_idx + 2, mid + 1, end)
        self.tree[node_idx] = self._combine(
            self.tree[2 * node_idx + 1],
            self.tree[2 * node_idx + 2],
        )

    def query(self, l: int, r: int) -> int:
        """Return the aggregate over the inclusive range [l, r]."""
        if l < 0 or r >= self.n or l > r:
            raise IndexError("query range must satisfy 0 <= l <= r < length")
        result = self._query(0, 0, self.n - 1, l, r)
        if result is None:
            raise RuntimeError("valid query unexpectedly returned no result")
        return result

    def _query(self, node_idx: int, start: int, end: int, l: int, r: int) -> int | None:
        if r < start or end < l:
            return None
        if l <= start and end <= r:
            return self.tree[node_idx]
        mid = (start + end) // 2
        left = self._query(2 * node_idx + 1, start, mid, l, r)
        right = self._query(2 * node_idx + 2, mid + 1, end, l, r)
        if left is None:
            return right
        if right is None:
            return left
        return self._combine(left, right)

    def update(self, idx: int, val: int) -> None:
        if idx < 0 or idx >= self.n:
            raise IndexError("update index out of range")
        self.arr[idx] = val
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node_idx: int, start: int, end: int, idx: int, val: int) -> None:
        if start == end:
            self.tree[node_idx] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node_idx + 1, start, mid, idx, val)
        else:
            self._update(2 * node_idx + 2, mid + 1, end, idx, val)
        self.tree[node_idx] = self._combine(
            self.tree[2 * node_idx + 1],
            self.tree[2 * node_idx + 2],
        )
