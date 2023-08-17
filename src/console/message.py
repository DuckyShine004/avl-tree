"""The module provides a way for the user to know whether the value they are
trying to add is valid or not."""
from __future__ import annotations

from enum import Enum


class Message(Enum):
    """Message allows for exceptions to be displayed to the terminal.

    Attributes:
        COMMON_VALUE_EXCEPTION (str): Exception occurs when value is not unique.
        NULL_VALUE_EXCEPTION (str): Exception occurs when value is null.
    """

    NULL_VALUE_EXCEPTION = "{value} IS NULL NODE"
    COMMON_VALUE_EXCEPTION = "NODE {value} IS ALREADY IN THE TREE"

    def print(self, message: str, value: int):
        """Print the message to the console.

        Args:
            message (str): The message or exception to be displayed to the console.
            value (int): The invalid value.
        """

        print(message.value.format(value=value), "\n")
