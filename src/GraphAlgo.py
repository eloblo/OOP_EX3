import json
from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from queue import PriorityQueue
import random
from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        if graph is None:
            self.graph = DiGraph()
        else:
            self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            json_file = open(file_name, "r")
            info = json_file.read()
            flag = True
            if info.find("pos") < 0:
                flag = False
            graph_dict = json.loads(info)
            new_graph = DiGraph()
            nodes = graph_dict["Nodes"]
            for n in nodes:
                if flag:
                    str_pos = n["pos"]
                    pos = tuple(map(float, str_pos.split(',')))
                    new_graph.add_node(n["id"], pos)
                else:
                    new_graph.add_node(n["id"])
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
        nodes = self.graph.get_all_v()
        comp = list()
        if len(nodes) == 0 or nodes.get(id1) is None:
            return comp
        self._clear_tag()
        que = list()
        que.append(nodes[id1])
        while len(que) != 0:
            node = que.pop(0)
            node.set_tag(1)
            edges = node.get_edges()
            for e in edges:
                if nodes[e].get_tag() == 0:
                    que.append(nodes[e])
        que.append(nodes[id1])
        while len(que) != 0:
            node = que.pop(0)
            node.set_tag(2)
            node.set_weight(1)
            back_edges = node.get_back_edges()
            for e in back_edges:
                if nodes[e].get_tag() == 1:
                    que.append(nodes[e])
        for n in nodes:
            if nodes[n].get_tag() == 2:
                comp.append(n)
        return comp

    def connected_components(self) -> List[list]:
        nodes = self.graph.get_all_v()
        comps = list()
        if len(nodes) == 0:
            return comps
        self._clear_weight()
        for n in nodes:
            node = nodes[n]
            if node.get_weight() != 1:
                com = self.connected_component(n)
                comps.append(com)
        return comps

    def plot_graph(self) -> None:
        nodes = self.graph.get_all_v()
        min_x, max_x, min_y, max_y = self._set_positions()
        if min_x == max_x or min_y == max_y:
            return
        print(min_x, max_x, min_y, max_y)
        r = min(max_x - min_x, max_y - min_y)/80
        fig, ax = plt.subplots(figsize=(6, 6))
        for n in nodes:
            node = nodes[n]
            pos = node.get_pos()
            circle = plt.Circle((pos[0], pos[1]), r)
            ax.add_artist(circle)
            ax.text(pos[0], pos[1], n)
            edges = node.get_edges()
            for e in edges:
                dest = nodes[e]
                dest_pos = dest.get_pos()
                ax.annotate("",
                            xy=(dest_pos[0], dest_pos[1]), xycoords='data',
                            xytext=(pos[0], pos[1]), textcoords='data',
                            arrowprops=dict(arrowstyle="->",
                                            connectionstyle="arc3"),
                            )
        r *= 10
        ax.axis([min_x-r, max_x+r, min_y-r, max_y+r])
        plt.show()

    def _set_positions(self):
        random.seed(10)
        nodes = self.graph.get_all_v()
        min_x = float('inf')
        min_y = float('inf')
        max_x = 0
        max_y = 0
        for n in nodes:
            node = nodes[n]
            pos = node.get_pos()
            if pos is not None:
                min_x = min(min_x, pos[0])
                min_y = min(min_y, pos[1])
                max_x = max(max_x, pos[0])
                max_y = max(max_y, pos[1])
        if min_x >= max_x:
            min_x = 0
            min_y = 0
            max_x = len(nodes)
            max_y = len(nodes)
        for n in nodes:
            node = nodes[n]
            pos = node.get_pos()
            if pos is None:
                x = random.uniform(min_x, max_x)
                y = random.uniform(min_y, max_y)
                new_pos = (x, y, 0)
                node.set_pos(new_pos)
        return min_x, max_x, min_y, max_y

    def _clear_tag(self):
        nodes = self.graph.get_all_v()
        for n in nodes:
            nodes[n].set_tag(0)

    def _clear_weight(self):
        nodes = self.graph.get_all_v()
        for n in nodes:
            nodes[n].set_weight(0)
