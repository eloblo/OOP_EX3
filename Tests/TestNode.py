import unittest
from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    # test addition and removal of edges
    def test_edges(self):
        node = DiGraph.Node(0, None)

        self.assertFalse(node.add_edge(0, 100))   # check false addition
        self.assertTrue(node.add_edge(1, 10))
        self.assertTrue(node.add_edge(2, 20))
        self.assertTrue(node.add_back_edge(2, 30))

        # check if edge dictionary is correct
        node_dict = node.get_edges()
        self.assertIsNone(node_dict.get(0))
        self.assertEqual(node_dict.get(1), 10)
        self.assertEqual(node_dict.get(2), 20)

        node_dict = node.get_back_edges()
        self.assertEqual(node_dict.get(2), 30)

        self.assertFalse(node.remove_edge(5))
        self.assertFalse(node.remove_edge(0))
        self.assertTrue(node.remove_edge(1))

        # check new dictionary values
        node_dict = node.get_edges()
        self.assertIsNone(node_dict.get(5))
        self.assertIsNone(node_dict.get(0))
        self.assertIsNone(node_dict.get(1))
        self.assertEqual(node_dict.get(2), 20)

    def test_path(self):    # test path function
        node = DiGraph.Node(0)
        p = [1, 2, 3]
        node.set_path(p)
        np = node.get_path()
        # check the node's path values
        for i in range(len(np)):
            self.assertEqual(p[i], np[i])
        node.set_path()
        p = list()
        np = node.get_path()
        for i in range(len(p)):
            self.assertEqual(p[i], np[i])


if __name__ == '__main__':
    unittest.main()
