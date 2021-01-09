import json
from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            json_file = open(file_name, "r")
            info = json_file.read()
            graph_dict = json.loads(info)
            new_graph = DiGraph()
            nodes = graph_dict["Nodes"]
            for n in nodes:
                str_pos = n["pos"]
                pos = tuple(map(float, str_pos.split(',')))
                new_graph.add_node(n["id"], pos)
            edges = graph_dict["Edges"]
            for e in edges:
                new_graph.add_edge(e["src"], e["dest"], e["w"])
            self.graph = new_graph
            json_file.close()
            return True
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            json_file = open(file_name, "w")
            info = repr(self.graph)
            json_file.write(info)
            json_file.close()
            return True
        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def _clear_tag(self):
        nodes = self.graph.get_all_v()
        for n in nodes:
            nodes[n].set_tag(0)

    def _clear_weight(self):
        nodes = self.graph.get_all_v()
        for n in nodes:
            nodes[n].set_weight(0)
