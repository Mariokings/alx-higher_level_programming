#/usr/bin/puthon3
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
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
