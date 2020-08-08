from benedict import benedict
import pydot
import json
from collections import defaultdict


class Tree(object):

    def __init__(self, documents):
        super().__init__()
        self.max_depth = 0
        self.json_tree = self.create_json_tree(documents)

    def create_json_tree(self, documents):
        tree = benedict()
        max_depth = 0
        for document in documents:
            path = ""
            words = document.split()
            max_depth = max(max_depth, len(words))
            for node in words:
                path += f".{node}"
                tree[path+".counter"] = tree.get(path+".counter", 0)+1
        self.max_depth = max_depth
        return tree[""]

    def draw(self, parent_name, child_name):
        edge = pydot.Edge(parent_name, child_name)
        self.graph.add_edge(edge)

    def populate_graph(self, node, parent=None, depth=4):
        for k, v in node.items():
            if k != 'counter':
                if depth == 0:
                    return None
                if isinstance(v, dict):
                    # We start with the root node whose parent is None
                    # we don't want to graph the None node
                    if parent:
                        self.draw(parent, k)
                    self.populate_graph(v, k, depth-1)
                else:
                    self.draw(parent, k)
                    # drawing the label using a distinct name
                    if v:
                        self.draw(k, k+'_'+v)

    def write_tree(self, name, depth, graph_type="digraph", simplify=True):
        depth = min(depth, self.max_depth)
        self.graph = pydot.Dot(graph_type=graph_type, simplify=simplify)
        self.populate_graph(self.json_tree, depth=depth)
        self.graph.write_png(name)
