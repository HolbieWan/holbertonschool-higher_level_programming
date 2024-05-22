#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        __width (int): The size of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with an optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width ot height is less than 0.
        """
        self.width = width
        self.height = height

    """Function to retrieve the value of the width attribute"""
    @property
    def width(self):
        return self.__width

    """Function to set the value of the width attribute """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Function to retrieve the value of the height attribute"""
    @property
    def height(self):
        return self.__height

    """Function to set the value of the width attribute """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
