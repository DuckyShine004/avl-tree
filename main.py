"""The main module and where the top-level code is run.
"""
import os

os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin/"

from src.tree.avl_tree import AVLTree


def main() -> None:
    """The main function. Call objects and methods here."""

    # Create a new tree
    tree = AVLTree()

    # Add values to the tree
    for i in range(20):
        tree.add(i)

    # Print the tree
    tree.print()

    # Remove a node with two descendants
    tree.remove(7)

    # Display the tree in terminal
    tree.print()

    # Display the tree with graphviz
    tree.graph()


if __name__ == "__main__":
    main()
