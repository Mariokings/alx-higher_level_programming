#!/usr/bin/python3
"""Square class definition """


class Square:
    """Represents a square class
    Attributes:
        size (int): size of a side of he square
    """
    def __init__(self, size=0):
        """Initializing a square
        Args:
            size (int): size of a side of the square
        Returns: current square area
        """
        try:
            assert type(size) == int
        except AssertionError:
            raise TypeError("size must be an integer")
        try:
            assert size >= 0
        except AssertionError:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
