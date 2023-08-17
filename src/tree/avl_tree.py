"""Summary."""
from __future__ import annotations

from src.tree.node import Node

from src.console.message import Message
from src.console.display_tree import DisplayTree

class AVLTree:
    """Summary.

    Attributes:
        balance_factor (int): Description
        root (TYPE): Description

    Deleted Attributes:
        cache (TYPE): Description
    """

    def __init__(self):
        """Summary."""
        self.root = None

        # Initially, the balance factor will be zero (tree is balanced)
        self.balance_factor = 0

    def add(self, value: int) -> None:
        """Summary.

        Args:
            value (int): Description

        Returns:
            None: Description

        Deleted Parameters:
            node (Node): Description
        """

        # Check if the value is null
        if value is None:
            Message.print(Message.NULL_VALUE_EXCEPTION, value)
            return

        # Check if the value is unique
        if not self.contains(value):
            # Check if a root exists
            if not self.root:
                self.root = Node(value)
                return

            # Add the value to the tree.
            self.root = self.__add(self.root, value)
            return

        # The value was not unique
        Message.print(Message.COMMON_VALUE_EXCEPTION, value)
        return

    def __add(self, node: Node, value: int) -> None:
        """Summary.

        Args:
            node (Node): Description
            value (int): Description

        Returns:
            None: Description
        """

        # Base case
        if not node:
            return Node(value)

        # Insert the node to the correct place in the tree
        if value < node.value:
            node.left = self.__add(node.left, value)
        else:
            node.right = self.__add(node.right, value)

        # Update the height of all affected nodes
        self.update(node)

        # Rebalance all affected nodes
        return self.balance(node)

    def contains(self, value: int):
        """Summary.

        Args:
            value (int): Description

        Returns:
            TYPE: Description
        """
        return self.__contains(self.root, value)

    def __contains(self, node: Node, value: int):
        """Summary.

        Args:
            node (Node): Description
            value (int): Description

        Returns:
            TYPE: Description
        """
        # Base case, if the current node is empty, backtrack
        if not node:
            return False

        # Check if the value is already in the tree
        if node.value == value:
            return True

        # Check the left subtree
        if self.__contains(node.left, value):
            return True

        # Check the right subtree
        if self.__contains(node.right, value):
            return True

    def update(self, node: Node) -> None:
        """Summary.

        Args:
            node (Node): Description
        """

        # Get the heights of the left and right subtrees. -1 indicates the node does not have subtrees.
        left_height = -1 if not node.left else node.left.height
        right_height = -1 if not node.right else node.right.height

        # Update the height of the current node
        node.height = 1 + max(left_height, right_height)

        # Update the balance factor of the current node
        node.balance_factor = right_height - left_height

    def balance(self, node: Node) -> Node:
        """Summary.

        Args:
            node (Node): Description

        Returns:
            Node: Description
        """

        # Check the left subtree
        if node.balance_factor == -2:
            if node.left.balance_factor <= 0:
                return self.left_left_case(node)
            else:
                return self.left_right_case(node)

        # Check the right subtree
        if node.balance_factor == 2:
            if node.right.balance_factor >= 0:
                return self.right_right_case(node)
            else:
                return self.right_left_case(node)

        # The node has a balance factor or [-1,0,1], meaning the node is already balanced
        return node

    def left_left_case(self, node: Node) -> Node:
        """Summary.

        Args:
            node (Node): Description

        Returns:
            Node: Description
        """
        return self.right_rotation(node)

    def left_right_case(self, node: Node) -> Node:
        """Summary.

        Args:
            node (Node): Description

        Returns:
            Node: Description
        """
        node.left = self.left_rotation(node.left)

        return self.left_left_case(node)

    def right_right_case(self, node: Node) -> Node:
        """Summary.

        Args:
            node (Node): Description

        Returns:
            Node: Description
        """

        return self.left_rotation(node)

    def right_left_case(self, node: Node) -> Node:
        """Summary.

        Args:
            node (Node): Description

        Returns:
            Node: Description
        """

        node.right = self.right_rotation(node.right)

        return self.right_right_case(node)

    def left_rotation(self, node: Node) -> Node:
        """Perform a left rotation for the current node. Aftwerwards, update
        the height and balance factor for the affected nodes, the parent
        node and the current node, respectively.

        Args:
            node (Node): Description

        Returns:
            Node: Description
        """

        parent = node.right
        node.right = parent.left
        parent.left = node

        self.update(node)
        self.update(parent)

        return parent

    def right_rotation(self, node: Node) -> Node:
        """Perform a righht rotation for the current node. Aftwerwards, update
        the height and balance factor for the affected nodes, the parent
        node and the current node, respectively.

        Args:
            node (Node): Description

        Returns:
            Node: Description
        """

        parent = node.left
        node.left = parent.right
        parent.right = node

        self.update(node)
        self.update(parent)

        return parent

    def print(self) -> None:
        """Displays the binary tree to the terminal. Best used when there are not a lot of values to display.
        """

        DisplayTree.print_tree(self.root, lambda node: (str(node.value), node.left, node.right))
