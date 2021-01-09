import json

from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.ec = 0
        self.nodes = dict()

    def v_size(self):
        return len(self.nodes)

    def e_size(self) -> int:
        return self.ec

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.nodes.get(id1) is not None:
            return self.nodes.get(id1).get_back_edges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.nodes.get(id1) is not None:
            return self.nodes.get(id1).get_edges()

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2 or weight <= 0:
            return False
        if self.nodes.get(id1) is not None and self.nodes.get(id2) is not None:
            src = self.nodes.get(id1)
            dest = self.nodes.get(id2)
            if src.add_edge(id2, weight) and dest.add_back_edge(id1, weight):
                self.ec += 1
                self.mc += 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id) is None:
            node = self.Node(node_id, pos)
            self.nodes.update([(node_id, node)])
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.get(node_id) is not None:
            node = self.nodes.get(node_id)
            edges = node.get_edges()
            back_edges = node.get_back_edges()
            self.ec -= (len(edges) + len(back_edges))
            self.mc += (len(edges) + len(back_edges) + 1)
            for n in edges:
                self.nodes.get(n).remove_back_edge(node_id)
            for n in back_edges:
                self.nodes.get(n).remove_edge(node_id)
            self.nodes.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 == node_id2:
            return False
        if self.nodes.get(node_id1) is not None and self.nodes.get(node_id2) is not None:
            src = self.nodes.get(node_id1)
            dest = self.nodes.get(node_id2)
            if src.remove_edge(node_id2) and dest.remove_back_edge(node_id1):
                self.ec -= 1
                self.mc += 1
                return True
        return False

    def get_graph(self):
        node_list = []
        edge_list = []
        for n in self.nodes:
            node = self.nodes[n].get_node()
            node_list.append(node)
            edges = self.nodes[n].get_edge_list()
            edge_list.extend(edges)
        graph_dict = {"Edges": edge_list, "Nodes": node_list}
        return graph_dict

    def __repr__(self):
        info = json.dumps(self.get_graph())
        return info

    #    ###########__Node_class__############

    class Node:

        def __init__(self, key, pos=None):
            self.key = key
            self.tag = 0
            self.path = list()
            self.weight = 0
            self.pos = pos
            self.edges = dict()
            self.back_edges = dict()

        def get_key(self):
            return self.key

        def add_edge(self, key, weight):
            if key != self.key and self.edges.get(key) is None:
                self.edges.update([(key, weight)])
                return True
            return False

        def add_back_edge(self, key, weight):
            if key != self.key and self.back_edges.get(key) is None:
                self.back_edges.update([(key, weight)])
                return True
            return False

        def remove_edge(self, key):
            if self.edges.get(key) is not None:
                self.edges.pop(key)
                return True
            return False

        def remove_back_edge(self, key):
            if self.back_edges.get(key) is not None:
                self.back_edges.pop(key)
                return True
            return False

        def get_edges(self):
            return self.edges

        def get_back_edges(self):
            return self.back_edges

        def get_path(self):
            return self.path

        def set_path(self, path=None):
            if path is None:
                self.path = list()
            else:
                self.path = path

        def append_path(self, key):
            self.path.append(key)

        def get_tag(self):
            return self.tag

        def set_tag(self, tag):
            self.tag = tag

        def get_weight(self):
            return self.weight

        def set_weight(self, weight):
            self.weight = weight

        def get_node(self):
            if self.pos is None:
                node_dict = {"id": self.key}
            else:
                str_pos = "%d,%d,%d" % (self.pos[0], self.pos[1], self.pos[2])
                node_dict = {"pos": str_pos, "id": self.key}
            return node_dict

        def get_edge_list(self):
            edge_list = []
            for e in self.edges:
                edge_dict = {"src": self.key, "w": self.edges[e], "dest": e}
                edge_list.append(edge_dict)
            return edge_list

        def __lt__(self, other):
            return self.weight - other.get_weight()

        def __repr__(self):
            info = json.dumps(self.get_node())
            return info
