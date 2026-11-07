import unittest

from maxflow import maxflow


class MaxFlowTests(unittest.TestCase):
    def test_single_edge(self):
        self.assertEqual(maxflow(10, [(2, 8, 7)], 2, 8), 7)

    def test_path_flow_is_limited_by_bottleneck(self):
        edges = [(0, 1, 5), (1, 3, 3)]

        self.assertEqual(maxflow(4, edges, 0, 3), 3)

    def test_combines_flow_from_multiple_paths(self):
        edges = [
            (0, 1, 3),
            (0, 2, 2),
            (1, 2, 1),
            (1, 3, 2),
            (2, 3, 3),
        ]

        self.assertEqual(maxflow(4, edges, 0, 3), 5)

    def test_parallel_edges_contribute_capacity(self):
        edges = [(0, 1, 2), (0, 1, 3)]

        self.assertEqual(maxflow(2, edges, 0, 1), 5)

    def test_returns_zero_when_sink_is_unreachable(self):
        edges = [(0, 1, 4), (2, 3, 7)]

        self.assertEqual(maxflow(4, edges, 0, 3), 0)

    def test_classic_network_with_residual_rerouting(self):
        edges = [
            (0, 1, 16),
            (0, 2, 13),
            (1, 2, 10),
            (2, 1, 4),
            (1, 3, 12),
            (3, 2, 9),
            (2, 4, 14),
            (4, 3, 7),
            (3, 5, 20),
            (4, 5, 4),
        ]

        self.assertEqual(maxflow(6, edges, 0, 5), 23)


if __name__ == "__main__":
    unittest.main()
