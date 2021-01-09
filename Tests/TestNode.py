import unittest
from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def test_edges(self):
        node = DiGraph.Node(0, None)

        node.add_edge(0,100)
        node.add_edge(1,10)
        node.add_edge(2,20)
        node.add_back_edge(2,30)

        node_dict = node.get_edges()
        self.assertIsNone(node_dict.get(0))
        self.assertEqual(node_dict.get(1), 10)
        self.assertEqual(node_dict.get(2), 20)

        node_dict = node.get_back_edges()
        self.assertEqual(node_dict.get(2), 30)

        node.remove_edge(5)
        node.remove_edge(0)
        node.remove_edge(1)

        node_dict = node.get_edges()
        self.assertIsNone(node_dict.get(5))
        self.assertIsNone(node_dict.get(0))
        self.assertIsNone(node_dict.get(1))
        self.assertEqual(node_dict.get(2), 20)

    def test_json(self):
        node1 = DiGraph.Node(1,None)
        node2 = DiGraph.Node(2,(1,2,3))
        node1.add_edge(2,2)
        node1.add_edge(3,1)
        node2.add_edge(4, 0)
        node2.add_edge(5, 10)
        print(node1.get_node())
        print(node1.get_edge_list())
        print(node2.get_node())
        print(node2.get_edge_list())

    def test_path(self):
        node = DiGraph.Node(0)
        p = [1, 2, 3]
        node.set_path(p)
        np = node.get_path()
        for i in range(len(np)):
            self.assertEqual(p[i], np[i])
        node.set_path()
        p = list()
        np = node.get_path()
        for i in range(len(p)):
            self.assertEqual(p[i], np[i])

if __name__ == '__main__':
    unittest.main()
