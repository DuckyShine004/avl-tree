"""This module allows the user to display the graph with graphviz."""
from graphviz import Digraph

from src.tree.node import Node


class GraphTree:
    """The binary will be visually represented using graphviz."""
    
    def display_tree(node: Node) -> None:
        """Display the binary tree using graphviz.

        Args:
            node (Node): The root node.
        """

        graph = Digraph()
        graph.node(str(node.value))

        def traverse(node: Node) -> None:
            """Recursively traverse the left and right subtrees, adding edges
            and nodes on the way to grpahviz's graph. Afterwards, render the
            image to the screen.

            Args:
                node (Node): The current node.
            """

            if node.left:
                graph.node(str(node.left.value))
                graph.edge(str(node.value), str(node.left.value))
                traverse(node.left)
            if node.right:
                graph.node(str(node.right.value))
                graph.edge(str(node.value), str(node.right.value))
                traverse(node.right)

        traverse(node)

        graph.render(view=True, format="png")
