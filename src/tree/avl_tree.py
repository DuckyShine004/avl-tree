"""This module allows the user to create an AVL tree."""
from __future__ import annotations

from src.tree.node import Node

from src.console.message import Message
from src.console.display_tree import DisplayTree


class AVLTree:
    """An AVL tree is a self-balancing binary search tree. In an AVL tree, the heights of the two
    child subtrees of any node differ by at most one; if at any time they differ by more than one,
    rebalancing is done to restore this property. Source: https://en.wikipedia.org/wiki/AVL_tree.

    Attributes:
        balance_factor (int): The difference between the height of the left subtree and that of the
        root (Node): The root of the binary tree.
        right subtree of a node.
    """

    def __init__(self):
        """Initialize the AVL tree."""

        self.root = None
        self.balance_factor = 0

    def add(self, value: int) -> None:
        """Adds the queried value to the binary tree if it is valid. The value
        is valid if the value is not null and it is unique. Display an
        exception message if the value is invalid.

        Args:
            value (int): The value to be added to the tree.

        Returns:
            None: Nothing is returned.
        """

        if value is None:
            Message.print(Message.NULL_VALUE_EXCEPTION)
            return None

        if not self.contains(value):
            if not self.root:
                self.root = Node(value)
                return None

            self.root = self.__add(self.root, value)
            return None

        Message.print(Message.COMMON_VALUE_EXCEPTION)
        return None

    def __add(self, node: Node, value: int) -> Node:
        """Adds the queried value to the binary tree. It calls itself
        recursively to determine where in the binary should the value be
        inserted. The base case is if we have reached an empty or null node,
        that means we have found the correct subtree, and hence, the correct
        place to insert the node. Afterwards, we backtrack and update the
        heights and rebalance all affected nodes (if needed). The new root will
        be the determined after rotations (if any).

        Args:
            node (Node): Initally, the root node.
            value (int): The value to be added to the tree.

        Returns:
            Node: The root node after rebalancing the tree.
        """

        if not node:
            return Node(value)

        if value < node.value:
            node.left = self.__add(node.left, value)
        else:
            node.right = self.__add(node.right, value)

        self.update(node)

        return self.balance(node)

    def contains(self, value: int) -> bool:
        """Determine whether the queried value exists within the tree.

        Args:
            value (int): The value queried.

        Returns:
            bool: A boolean value based on whether the value exists or not.
        """

        return self.__contains(self.root, value)

    def __contains(self, node: Node, value: int) -> bool:
        """Recrusively search the left and right subtree to check if the value
        exists within the binary tree. The base case is if we have reached an
        empty node, we return false, because a null node indicates that we have
        reached the end of a subtree, therefore, the value does not exist in
        the subtree.

        Args:
            node (Node): The current node.
            value (int): The value queried.

        Returns:
            bool: A boolean value based on whether the value exists or not.
        """

        if not node:
            return False

        if node.value == value:
            return True

        if self.__contains(node.left, value):
            return True

        if self.__contains(node.right, value):
            return True

    def update(self, node: Node) -> None:
        """Update the height and balance factor for the current node. Retrieve
        the left subtree height and the right subtree height. Then the height
        of the current node will be the maximum between the two subtree heights
        + 1 (we still have to consider the current node!) as per the definition
        of 'height' in the context of binary trees. The balance factor is simply the difference
        between the heights of the two subtrees, as per the definition.

        Args:
            node (Node): The node to be updated.
        """

        left_height = -1 if not node.left else node.left.height
        right_height = -1 if not node.right else node.right.height

        node.height = 1 + max(left_height, right_height)
        node.balance_factor = right_height - left_height

    def balance(self, node: Node) -> Node:
        """Rebalances the tree if any balancing is needed at all. There are.

        four cases to consider:
            1. The tree is heavily unbalanced to the left (left-left case). Performed when the node
            is inserted into the right subtree leading to an unbalanced tree. This is a single left
            rotation to make the tree balanced again.

            2. The tree is heavily unbalanced to the right (right-right case). Performed when the
            node is inserted into the right subtree leading to an unbalanced tree. This is a single
            left rotation to make the tree balanced again.

            3. Tree is unbalanced (left-right case), a node is inserted into the right subtree of
            the left subtree. Simply call a right rotation followed by a left rotation to maintain
            balance again.

            4. Tree is unbalanced (right-left case), a node is inserted into the right subtree of
            the left subtree. Simple call a left rotation followed by a right rotation to maintain
            balance again.

            Otherwise, the node has a balance factor of values in [-1, 0, 1], meaning the node is
            already balanced.

        Args:
            node (Node): Rhe node to be balanced.

        Returns:
            Node: The new root node.
        """

        if node.balance_factor == -2:
            if node.left.balance_factor <= 0:
                return self.left_left_case(node)

            return self.left_right_case(node)

        if node.balance_factor == 2:
            if node.right.balance_factor >= 0:
                return self.right_right_case(node)

            return self.right_left_case(node)

        return node

    def left_left_case(self, node: Node) -> Node:
        """The tree is heavily unbalanced to the left (left-left case).
        Performed when the node is inserted into the right subtree leading to
        an unbalanced tree. This is a single left rotation to make the tree
        balanced again.

        Args:
            node (Node): The node to be rotated.

        Returns:
            Node: The new root.
        """

        return self.right_rotation(node)

    def left_right_case(self, node: Node) -> Node:
        """Tree is unbalanced (left-right case), a node is inserted into the
        right subtree of the left subtree. Simply call a right rotation
        followed by a left rotation to maintain balance again.

        Args:
            node (Node): The node to be rotated.

        Returns:
            Node: The new root.
        """

        node.left = self.left_rotation(node.left)

        return self.left_left_case(node)

    def right_right_case(self, node: Node) -> Node:
        """The tree is heavily unbalanced to the right (right-right case).
        Performed when the node is inserted into the right subtree leading to
        an unbalanced tree. This is a single left rotation to make the tree
        balanced again.

        Args:
            node (Node): The node to be rotated.

        Returns:
            Node: The new root.
        """

        return self.left_rotation(node)

    def right_left_case(self, node: Node) -> Node:
        """Tree is unbalanced (right-left case), a node is inserted into the
        right subtree of the left subtree. Simple call a left rotation followed
        by a right rotation to maintain balance again.

        Args:
            node (Node): The node to be rotated.

        Returns:
            Node: The new root.
        """

        node.right = self.right_rotation(node.right)

        return self.right_right_case(node)

    def left_rotation(self, node: Node) -> Node:
        """Perform a left rotation for the current node. Aftwerwards, update
        the height and balance factor for the affected nodes, the parent node
        and the current node, respectively.

        Args:
            node (Node): The node to be left rotated.

        Returns:
            Node: Returns the parent of the queried node.
        """

        parent = node.right
        node.right = parent.left
        parent.left = node

        self.update(node)
        self.update(parent)

        return parent

    def right_rotation(self, node: Node) -> Node:
        """Perform a right rotation for the current node. Aftwerwards, update
        the height and balance factor for the affected nodes, the parent node
        and the current node, respectively.

        Args:
            node (Node): The node to be right rotated.

        Returns:
            Node: Returns the parent of the queried node.
        """

        parent = node.left
        node.left = parent.right
        parent.right = node

        self.update(node)
        self.update(parent)

        return parent

    def print(self) -> None:
        """Displays the binary tree to the terminal.

        Best used when there are not a lot of values to display.
        """

        DisplayTree.print_tree(self.root, lambda node: (str(node.value), node.left, node.right))
