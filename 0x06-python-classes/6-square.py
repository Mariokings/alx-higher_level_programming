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
            position (int, int): tuple of two positive integer
        Returns: current square area
        """
        self.size = size
        self.position = position

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
        """Get/set the current position of the square """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value