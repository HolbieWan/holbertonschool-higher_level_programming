#!/usr/bin/python3
"""Abstract classes"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Class Shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Shape Subclass Circle"""

    def __init__(self, radius):
        """
        Initializes a new Circle instance with an optional radius
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        py_value = math.pi
        return (self.radius ** 2 * py_value)

    def perimeter(self):
        if self.radius < 0:
            raise ValueError(
                "Perimeter calculation cannot be performed for negative radius")
        py_value = math.pi
        return (self.radius * 2 * py_value)


class Rectangle(Shape):
    """Shape Subclass Rectangle"""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with an optional width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        py_value = math.pi
        return (self.width * self.height)

    def perimeter(self):
        return (self.height + self.width) * 2


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
