import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_load(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertTrue(ga.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\A5"))
        g = ga.get_graph()
        self.assertEqual(g.v_size(), 48)
        self.assertEqual(g.e_size(), 166)

    def test_save(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        for i in range(5):
            g.add_edge(i, i+1, i*10 + 1)
        ga1 = GraphAlgo(g)
        self.assertTrue(ga1.save_to_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\test.json"))

        ga2 = GraphAlgo(DiGraph())
        ga2.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\test.json")

        self.assertEqual(repr(ga1.get_graph()), repr(ga2.get_graph()))


if __name__ == '__main__':
    unittest.main()
