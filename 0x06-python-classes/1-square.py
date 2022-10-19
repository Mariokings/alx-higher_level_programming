#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """Represents a Square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializing square
        Args:
            self (int): size of a side of the square
        Returns: None
        """
        self.__size = size
