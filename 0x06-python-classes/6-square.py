#!/usr/bin/python3
"""Square class definition """


class Square:
    """Represents a square class
    Attributes:
        size (int): size of a side of he square
        position (tuple): tuple of two positive integer
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializing a square
        Args:
            size (int): size of a side of the square
            position (tuple): tuple of two positive integer
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
        try:
            assert type(position) == tuple and type(position[0]) == int
        except AttributeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert position[0] >= 0 and type(position[-1]) == int
        except AttributeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert position[-1] >= 0
        except AttributeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert len(position) == 2
        except AttributeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            assert type(value) == int
        except AssertionError:
            raise TypeError("size must be an integer")
        try:
            assert value >= 0
        except AssertionError:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    for j in range(self.__position[0]):
                        print("_", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            assert type(value) == tuple and type(value[0]) == int
        except AttributeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert value[0] >= 0 and type(value[-1]) == int and value[-1] >= 0
        except AttributeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert len(value) == 2
        except AttributeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
