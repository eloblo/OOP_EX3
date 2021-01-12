import unittest
import networkx as nx
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from Tests.NXJsonReader import NXJsonReader


class MyTestCase(unittest.TestCase):
    def test_load(self):   # test the loading from files
        g = DiGraph()
        ga = GraphAlgo(g)
        # load large graph
        self.assertTrue(ga.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\A5"))
        g = ga.get_graph()
        # check values
        self.assertEqual(g.v_size(), 48)
        self.assertEqual(g.e_size(), 166)

    def test_save(self):    # test saving the graph to a file
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        for i in range(5):
            g.add_edge(i, i+1, i*10 + 1)
        ga1 = GraphAlgo(g)
        # check if saving was successful
        self.assertTrue(ga1.save_to_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\test.json"))

        # load a new graph from the saved file and compare graphs
        ga2 = GraphAlgo(DiGraph())
        ga2.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\test.json")
        self.assertEqual(repr(ga1), repr(ga2))

        # test on a large graph
        ga1.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\data\\G_100_800_1.json")
        self.assertTrue(ga1.save_to_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\test.json"))
        ga2.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\test.json")
        self.assertEqual(repr(ga1), repr(ga2))

    def test_shortest_path(self):   # test the shortest path and distance
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        for i in range(9):
            g.add_edge(i, i+1, 1)
        g.add_edge(0, 9, 100)
        g.add_edge(0, 6, 3)
        g.add_edge(6, 8, 2)
        ga = GraphAlgo(g)
        dist, path = ga.shortest_path(0, 9)
        self.assertEqual(dist, 6)    # check distance
        check = [0, 6, 8, 9]
        for i in range(len(check)):    # check path
            self.assertEqual(check[i], path[i])

        check = [7]
        dist, path = ga.shortest_path(7, 7)
        self.assertEqual(dist, 0)        # check algorithm for single node path
        for i in range(len(check)):
            self.assertEqual(check[i], path[i])

        dist, path = ga.shortest_path(8, 5)    # check for invalid parameters
        self.assertEqual(dist, float('inf'))
        self.assertEqual(len(path), 0)

        # check on a heavy graph against networkx

        nxr = NXJsonReader()
        nxr.read("C:\\Users\\User\\PycharmProjects\\Ex3\\data\\G_100_800_1.json")
        nxg = nxr.get_graph()
        nx_path = nx.shortest_path(nxg, 3, 73, weight="weight")
        nx_dist = nx.shortest_path_length(nxg, 3, 73, weight="weight")

        ga = GraphAlgo()
        ga.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\data\\G_100_800_1.json")
        dist, path = ga.shortest_path(3, 73)

        self.assertEqual(dist, nx_dist)
        self.assertEqual(path, nx_path)

    def test_connected_component(self):    # test component
        g = DiGraph()
        for i in range(4):
            g.add_node(i)
        g.add_edge(1, 2, 2)
        g.add_edge(2, 1, 1)
        ga = GraphAlgo(g)
        # check correction of the return values of multiple node component
        check = [1, 2]
        comp = ga.connected_component(1)
        for i in range(len(comp)):
            self.assertEqual(check[i], comp[i].get_key())
        # check correction of the return values of single node component
        check = [3]
        comp = ga.connected_component(3)
        for i in range(len(comp)):
            self.assertEqual(check[i], comp[i].get_key())
        # # check correction of the return values invalid parameters
        comp = ga.connected_component(5)
        self.assertEqual(len(comp), 0)

    def test_connected_components(self):   # test connected components
        g = DiGraph()
        for i in range(4):
            g.add_node(i)
        g.add_edge(1, 2, 2)
        g.add_edge(2, 1, 1)
        ga = GraphAlgo(g)
        # check correction of values for simple and small graph
        check = [[0], [1, 2], [3]]
        comps = ga.connected_components()
        for c in range(len(comps)):
            com = comps[c]
            for n in range(len(com)):
                self.assertEqual(com[n].get_key(), check[c][n])
        # check correction of values in a big connected graph
        ga.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\A5")
        comps = ga.connected_components()
        com = comps[0]
        for n in range(len(com)):
            self.assertEqual(com[n].get_key(), n)
        # check correction against networkx
        nxr = NXJsonReader()
        nxr.read("C:\\Users\\User\\PycharmProjects\\Ex3\\data\\G_10000_80000_1.json")
        nxg = nxr.get_graph()
        nx_comps = nx.strongly_connected_components(nxg)
        ga.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\data\\G_10000_8000_1.json")
        comps = ga.connected_components()
        # convert the returned values to list of lists of integers
        nx_list = list()
        ga_list = list()
        for nxc in nx_comps:
            sub_list = list()
            for n in nxc:
                sub_list.append(n)
            sub_list.sort()
            nx_list.append(sub_list)
        for c in comps:
            sub_list = list()
            for n in c:
                sub_list.append(n.get_key())
            sub_list.sort()
            ga_list.append(sub_list)
        # sort and compare results
        ga_list.sort()
        nx_list.sort()
        for sub in range(len(ga_list)):
            for n in range(len(ga_list[sub])):
                self.assertEqual(ga_list[sub][n], nx_list[sub][n])

    def test_plot(self):    # test plotting
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        for i in range(6):
            g.add_edge(i+1, i+2, (i+1)*10)
        ga = GraphAlgo(g)
        ga.plot_graph()   # plot simple graph with no position
        # plot big graph with positions
        ga.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\A5")
        ga.plot_graph()
        # plot big graph with no positions
        ga.load_from_json("C:\\Users\\User\\PycharmProjects\\Ex3\\Data\\G_10_80_0.json")
        ga.plot_graph()


if __name__ == '__main__':
    unittest.main()
