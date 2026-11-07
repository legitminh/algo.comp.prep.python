import unittest

from kosaraju.kosaraju import kosaraju


class FunctionalKosarajuTests(unittest.TestCase):
    def test_groups_mutually_reachable_vertices(self):
        graph = {
            1: [2],
            2: [1, 3],
            3: [4],
            4: [3],
        }

        component_ids = kosaraju(graph, set(graph))

        self.assertEqual(component_ids[1], component_ids[2])
        self.assertEqual(component_ids[3], component_ids[4])
        self.assertNotEqual(component_ids[2], component_ids[3])

    def test_keeps_one_way_connected_vertices_in_separate_components(self):
        graph = {1: [2], 2: [3], 3: []}

        component_ids = kosaraju(graph, set(graph))

        self.assertEqual(set(component_ids), set(graph))
        self.assertEqual(len(set(component_ids.values())), 3)

    def test_includes_isolated_vertices(self):
        graph = {1: [], 2: []}

        component_ids = kosaraju(graph, set(graph))

        self.assertEqual(set(component_ids), {1, 2})
        self.assertNotEqual(component_ids[1], component_ids[2])

    def test_supports_negative_vertex_labels(self):
        graph = {-1: [2], 2: [-1, 3], 3: []}

        component_ids = kosaraju(graph, set(graph))

        self.assertEqual(component_ids[-1], component_ids[2])
        self.assertNotEqual(component_ids[2], component_ids[3])

    def test_empty_graph_has_no_components(self):
        self.assertEqual(kosaraju({}, set()), {})


if __name__ == "__main__":
    unittest.main()
