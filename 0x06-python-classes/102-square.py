#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Represents a square class."""

    def __init__(self, size=0):
        """Initializing square
        Args:
            size (int): size of square
        """
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """Get/set the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) != int or type(size) != float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Compare if square is less than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size
