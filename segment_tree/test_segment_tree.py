import unittest

from segment_tree import SegmentTree


class SegmentTreeTests(unittest.TestCase):
    def test_sum_query_reflects_updates(self):
        tree = SegmentTree([2, 1, 5, 3], operation="sum")

        self.assertEqual(tree.query(1, 3), 9)

        tree.update(2, -4)

        self.assertEqual(tree.query(1, 3), 0)
        self.assertEqual(tree.query(0, 3), 2)

    def test_sum_query_after_multiple_updates(self):
        tree = SegmentTree([4, 0, -2, 7, 1], operation="sum")

        tree.update(1, 6)
        tree.update(4, -3)

        self.assertEqual(tree.query(0, 2), 8)
        self.assertEqual(tree.query(2, 4), 2)

    def test_min_query_reflects_update_to_current_minimum(self):
        tree = SegmentTree([8, 3, 6, 2, 9], operation="min")

        self.assertEqual(tree.query(1, 4), 2)

        tree.update(3, 10)

        self.assertEqual(tree.query(1, 4), 3)
        self.assertEqual(tree.query(0, 4), 3)

    def test_min_query_after_multiple_updates(self):
        tree = SegmentTree([5, -1, 7, 4], operation="min")

        tree.update(1, 8)
        tree.update(2, -3)

        self.assertEqual(tree.query(0, 3), -3)
        self.assertEqual(tree.query(0, 1), 5)

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            SegmentTree([])


if __name__ == "__main__":
    unittest.main()
