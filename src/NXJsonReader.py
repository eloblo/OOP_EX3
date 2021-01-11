import json
import networkx as nx


class NXJsonReader:

    def __init__(self):
        self.graph = nx.DiGraph()

    def get_graph(self):
        return self.graph

    def read(self, file):
        json_file = open(file, "r")
        info = json_file.read()
        graph_dict = json.loads(info)

        nodes = graph_dict["Nodes"]
        for node in nodes:
            self.graph.add_node(node["id"])

        edges = graph_dict["Edges"]
        for edge in edges:
            self.graph.add_edge(edge["src"], edge["dest"], weight=edge["w"])
        json_file.close()
