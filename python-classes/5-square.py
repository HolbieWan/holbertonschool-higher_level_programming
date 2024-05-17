#!/usr/bin/python3
"""Class Square"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Function that returns the area of a square of size"""
        return self.__size ** 2

    """Function to retrieve the value of the size attribute"""
    @property
    def size(self):
        return self.__size

    """Function to set the value of the size attribute """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if (self.__size == 0):
            print('')
        for x in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print('')