#!/usr/bin/python3
"""Abstract classes"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Class Shape"""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Shape Subclass Circle"""

    def __init__(self, radius):
        """Initialize a new Circle instance with a given radius."""
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        py_value = math.pi
        return (self.radius ** 2 * py_value)

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        if self.radius < 0:
            raise ValueError(
                "Perimeter calculation cannot be performed for negative radius")
        py_value = math.pi
        return (self.radius * 2 * py_value)


class Rectangle(Shape):
    """Shape Subclass Rectangle"""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        py_value = math.pi
        return (self.width * self.height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return (self.height + self.width) * 2


def shape_info(shape):
    """Print the area and perimeter of the shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
