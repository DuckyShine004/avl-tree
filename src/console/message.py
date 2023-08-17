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

    NULL_VALUE_EXCEPTION = "PLEASE PROVIDE A NON-EMPTY NODE"
    VOID_VALUE_EXCEPTION = "PLEASE PROVIDE AN EXISITNG NODE"
    COMMON_VALUE_EXCEPTION = "NODE / VALUE IS ALREADY IN THE TREE"

    def print(message: str):
        """Print the message to the console.

        Args:
            message (str): The message or exception to be displayed to the console.
        """

        print(message.value, "\n")
