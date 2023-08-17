"""Summary
"""
from __future__ import annotations

from enum import Enum


class Message(Enum):
    """Summary.

    Attributes:
        COMMON_VALUE_EXCEPTION (str): Description
        NULL_VALUE_EXCEPTION (str): Description
    """

    NULL_VALUE_EXCEPTION = "{value} IS NULL NODE"
    COMMON_VALUE_EXCEPTION = "NODE {value} IS ALREADY IN THE TREE"

    def print(message: str, value: int):
        """Summary.

        Args:
            message (str): Description
            value (int): Description
        """

        print(message.value.format(value=value), "\n")
