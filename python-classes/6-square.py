#!/usr/bin/python3
"""Class Square"""


class Square:
    """Represents a square.
    Attributes: __size (int): The size of the square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with an optional size.
        Args: size (int, optional): The size of the square. Defaults to 0."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Function to retrieve the value of the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function to set the value of the size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter to set position"""
        if not isinstance(value(tuple)) or not isinstance(value(int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with char # """
        if (self.__size == 0):
            print('')
        for x in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print('')
