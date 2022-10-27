#!/usr/bin/python3
"""Defines a class for square"""


class Square:
    """Initialize a square.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position


    def area(self):
        """set/get the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """set/get the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set/get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not all(isinstance(value, tuple) and 
                value[0] is not int and value[-1] is not int):
            raise TypeError("position must be a tuple of 2 positive integer")
        slef.__value = value
