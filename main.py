"""Summary.
"""

from src.tree.avl_tree import AVLTree


def main() -> None:
    """The main function. Call objects and methods here."""

    # Create a new tree
    tree = AVLTree()

    # Add values to the tree
    for i in range(10):
        tree.add(i)

    # Display the tree in terminal
    tree.print()

    # Display the tree on webgraphviz
    # tree.graph()


if __name__ == "__main__":
    main()
