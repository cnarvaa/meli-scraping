from typing import List
from typing import Dict
from typing import Union

from benedict import benedict
import pydot


class Tree(object):
    """Class to manage tree creation and exporting
    """

    def __init__(self, documents: List[str]):
        """Initialize the Tree object creating the tree in dict format automatilly

        Args:
            documents (List[str]): documents to add into the tree
        """
        super().__init__()
        self.max_depth = 0
        self.json_tree = self.create_dict_tree(documents)

    def create_dict_tree(self, documents: List[str]):
        """Generate the tree in a dictionary structure.
        This tree will have a `counter` property in the edges (the connection between nodes)
        in order to facilitate filtering processes.

        this function modifies self.max_depth attribute with the max_depth found in the tree

        Args:
            documents (List[str]): documents to populate the tree

        Returns:
            benedict: a benedict dictionary with the extracted structure
        """
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

    def draw(self, parent_name: str, child_name: str):
        """create an edge for the drawing process

        Args:
            parent_name (str):
            child_name (str):
        """
        edge = pydot.Edge(parent_name, child_name)
        self.graph.add_edge(edge)

    def populate_graph(self, node: Dict, parent: Union[str, Dict] = None, depth: int = 4):
        """create the graph components based in an specified tree for the
        draw process

        Args:
            node (Dict): the tree to draw
            parent (str, optional): parent key, normally an string. Defaults to None.
            depth (int, optional): max depth you want to draw. Defaults to 4.

        Returns:
            None: modify the self.graph attribute
        """
        for key, value in node.items():
            if key != 'counter':
                if depth == 0:
                    return None
                if isinstance(value, dict):
                    # We start with the root node whose parent is None
                    # we don't want to graph the None node
                    if parent:
                        self.draw(parent, key)
                    self.populate_graph(value, key, depth-1)
                else:
                    self.draw(parent, key)
                    if value:
                        self.draw(key, key+'_'+value)

    def write_tree(self, name: str, depth: int, graph_type: str = "digraph", simplify: bool = True):
        """create an image in png format based in the generated tree

        Args:
            name (str): dir to write the image
            depth (int): depth of the tree. The smallest between this and the max_depth is used.
            graph_type (str, optional): can be graph or digraph. Defaults to "digraph".
            simplify (bool, optional): limit the number of edges in the image. Defaults to True.
        """
        depth = min(depth, self.max_depth)
        self.graph = pydot.Dot(graph_type=graph_type, simplify=simplify)
        self.populate_graph(self.json_tree, depth=depth)
        self.graph.write_png(name)
