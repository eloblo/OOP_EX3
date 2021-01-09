import json
from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from queue import PriorityQueue


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
        dist = 0
        path = list()
        nodes = self.graph.get_all_v()
        if nodes.get(id1) is not None and nodes.get(id2) is not None:
            if id1 == id2:
                return dist, path
            self._clear_weight()
            que = PriorityQueue()
            src = nodes.get(id1)
            path.append(id1)
            src.set_path(path)
            que.put(src)
            while not que.empty():
                node = que.get()
                if id2 == node.get_key():
                    dist = node.get_weight()
                    path = node.get_path()
                    return dist, path
                edges = node.get_edges()
                for e in edges:
                    ni = nodes[e]
                    dist = node.get_weight() + edges[e]
                    if (dist < ni.get_weight() or ni.get_weight() == 0) and ni.get_key() != id1:
                        temp_path = node.get_path().copy()
                        temp_path.append(e)
                        ni.set_path(temp_path)
                        ni.set_weight(dist)
                        que.put(ni)
        dist = float('inf')
        return dist, path

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
