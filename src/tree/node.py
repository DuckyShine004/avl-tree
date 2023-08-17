"""This module provides a way to create a node, which allows users to efficiently store and access 
data.
"""
from __future__ import annotations

from typing import Optional


class Node(object):
    """The node is a data structure which stores useful information related to
    an avl (self-balancing) tree.
    
    Attributes:
        height (int): The height of the node. The height is defined as the maximum path length of
        left (Node): The left child or descendant of the node.
        right (Node): The right child or descendant of the node.
        value (int): The value or key of the node.
        the node to a leaf of the tree.
    """

    def __init__(
        self,
        value: int,
        height: Optional[int] = 0,
        left: Optional[Node] = None,
        right: Optional[Node] = None,
    ) -> None:
        """Initialize the node.
        
        Args:
            value (int): The value or key of the node.
            height (Optional[int], optional): The height of the node. The height is defined as the
            left (Optional[Node], optional): The left child or descendant of the node.
            right (Optional[Node], optional): The right child or descendant of the node.
            maximum path length of the node to a leaf of the tree.
        """

        self.value = value
        self.height = height
        self.left = left
        self.right = right
