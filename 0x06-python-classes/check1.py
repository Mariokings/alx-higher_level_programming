#!/usr/bin/python3

"""Defines class for square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
    """Initialize a square.
        Args:
            size (int): Size of the square.
            position (int int): The position of the new square.
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif type(value[0]) is not int and type(value[-1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
    
    def area(self):
        """set/get the area of the square"""
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print("")
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
    
    def __str__(self):
        """Define the print() representation of a Square."""

        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ") for k in range(0, self.__position[0])]
            [print("#") for j in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
