#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        __width (int): The size of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

    def my_print(self):
        """Function that prints the rectangle"""
        i = 0
        j = 0
        if (self.__width == 0) or (self.__height == 0):
            print('')
            return
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

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

    def area(self):
        """Public instance method that returns the current rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Public instance method: returns the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for i in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """__repr__ method for rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is being deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a rectangle with width==height==size"""
        return cls(size, size)
