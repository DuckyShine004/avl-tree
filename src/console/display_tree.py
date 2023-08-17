"""Summary
"""
from __future__ import annotations

import functools

from typing import Optional

from src.tree.node import Node


class DisplayTree:

    """Allows the user to easily display the binary tree that they have created.
    """

    def print_tree(
        node: Node,
        node_info: Optional[str, Node, Node] = None,
        inverted: Optional[bool] = False,
        is_top: Optional[bool] = True,
    ) -> None:
        """Prints the binary tree to the terminal. The binary tree will be displayed vertically.
        
        Args:
            node (Node): a data structure which stores useful information related to an avl 
            node_info (Optional[str, Node, Node], optional): The string value of the node's integer 
            inverted (Optional[bool], optional): Do you want to display the tree top-down or 
            is_top (Optional[bool], optional): Description
            (self-balancing) tree.
            value.
            bottom-up.
        
        """

        string_value, left_node, right_node = node_info(node)

        string_value_width = len(string_value)

        left_text_block = (
            [] if not left_node else DisplayTree.print_tree(left_node, node_info, inverted, False)
        )
        right_text_block = (
            [] if not right_node else DisplayTree.print_tree(right_node, node_info, inverted, False)
        )

        common_lines = min(len(left_text_block), len(right_text_block))
        sub_level_lines = max(len(right_text_block), len(left_text_block))

        left_sub_lines = left_text_block + [""] * (sub_level_lines - len(left_text_block))
        right_sub_lines = right_text_block + [""] * (sub_level_lines - len(right_text_block))

        left_line_widths = [len(line) for line in left_sub_lines]
        right_line_indents = [len(line) - len(line.lstrip(" ")) for line in right_sub_lines]

        first_left_width = (left_line_widths + [0])[0]
        first_right_indent = (right_line_indents + [0])[0]

        link_spacing = min(string_value_width, 2 - string_value_width % 2)
        left_link_bar = 1 if left_node else 0
        right_link_bar = 1 if right_node else 0
        min_link_width = left_link_bar + link_spacing + right_link_bar
        value_offset = (string_value_width - link_spacing) // 2

        min_spacing = 2
        right_node_position = functools.reduce(
            lambda r, i: max(r, i[0] + min_spacing + first_right_indent - i[1]),
            zip(left_line_widths, right_line_indents[0:common_lines]),
            first_left_width + min_link_width,
        )

        link_extra_width = max(0, right_node_position - first_left_width - min_link_width)
        right_link_extra = link_extra_width // 2
        left_link_extra = link_extra_width - right_link_extra

        value_indent = max(0, first_left_width + left_link_extra + left_link_bar - value_offset)
        value_line = " " * max(0, value_indent) + string_value
        slash = "\\" if inverted else "/"
        backslash = "/" if inverted else "\\"
        u_line = "¯" if inverted else "_"

        left_link = (
            "" if not left_node else (" " * first_left_width + u_line * left_link_extra + slash)
        )

        right_link_offset = link_spacing + value_offset * (1 - left_link_bar)
        right_link = (
            ""
            if not right_node
            else (" " * right_link_offset + backslash + u_line * right_link_extra)
        )

        link_line = left_link + right_link

        left_indent_width = max(0, first_right_indent - right_node_position)
        left_indent = " " * left_indent_width
        indented_left_lines = [(left_indent if line else "") + line for line in left_sub_lines]

        merge_offsets = [len(line) for line in indented_left_lines]
        merge_offsets = [
            left_indent_width + right_node_position - first_right_indent - w for w in merge_offsets
        ]
        merge_offsets = [p if right_sub_lines[i] else 0 for i, p in enumerate(merge_offsets)]

        merged_sub_lines = zip(range(len(merge_offsets)), merge_offsets, indented_left_lines)
        merged_sub_lines = [(i, p, line + (" " * max(0, p))) for i, p, line in merged_sub_lines]
        merged_sub_lines = [
            line + right_sub_lines[i][max(0, -p) :] for i, p, line in merged_sub_lines
        ]

        tree_lines = (
            [left_indent + value_line]
            + ([] if not link_line else [left_indent + link_line])
            + merged_sub_lines
        )

        tree_lines = reversed(tree_lines) if inverted and is_top else tree_lines

        if is_top:
            print("\n".join(tree_lines))
        else:
            return tree_lines

        print()
