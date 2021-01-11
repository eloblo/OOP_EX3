import unittest
import networkx as nx
import time
from src.GraphAlgo import GraphAlgo
from src.NXJsonReader import NXJsonReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        nxr = NXJsonReader()
        file = "C:\\Users\\User\\PycharmProjects\\Ex3\\data\\G_30000_240000_1.json"
        nxr.read(file)
        self.nxg = nxr.get_graph()
        self.ga = GraphAlgo()
        self.ga.load_from_json(file)

    def test_nx_shortest(self):
        start = time.time()
        for i in range(10):
            nx.shortest_path(self.nxg, 1, 25468, weight="weight")
            nx.shortest_path_length(self.nxg, 1, 25468, weight="weight")
        end = time.time()
        print((end - start)/10)

    def test_nx_CC(self):
        start = time.time()
        for i in range(10):
            nx.strongly_connected_components(self.nxg)
        end = time.time()
        print((end - start)/10)

    def test_GA_shortest(self):
        start = time.time()
        for i in range(10):
            self.ga.shortest_path(1, 25468)
        end = time.time()
        print((end - start)/10)

    def test_GA_CCS(self):
        start = time.time()
        for i in range(10):
            self.ga.connected_components()
        end = time.time()
        print((end - start)/10)

    def test_GA_CC(self):
        start = time.time()
        for i in range(10):
            self.ga.connected_component(456)
        end = time.time()
        print((end - start)/10)


if __name__ == '__main__':
    unittest.main()
