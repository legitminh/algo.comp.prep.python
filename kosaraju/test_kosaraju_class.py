import unittest

from kosaraju.kosaraju_class import Graph


class KosarajuTests(unittest.TestCase):
    def test_finds_strongly_connected_components(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(2, 1)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 3)

        components = {frozenset(component) for component in graph.kosaraju_scc()}

        self.assertEqual(components, {frozenset({1, 2}), frozenset({3, 4})})

    def test_scc_dictionary_assigns_same_id_to_connected_vertices(self):
        graph = Graph()
        graph.add_edge(-1, 2)
        graph.add_edge(2, -1)
        graph.add_edge(2, 3)

        component_ids = graph.kosaraju_scc_dict()

        self.assertEqual(component_ids[-1], component_ids[2])
        self.assertNotEqual(component_ids[2], component_ids[3])
        self.assertEqual(set(component_ids), {-1, 2, 3})


if __name__ == "__main__":
    unittest.main()
