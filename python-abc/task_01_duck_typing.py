#!/usr/bin/python3
"""Abstract classes module."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass


class Circle(Shape):
    """A shape subclass representing a circle."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    @property
    def radius(self):
        """Return the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius ensuring it is non-negative."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    def area(self):
        """Return the area."""
        py_value = math.pi
        return self.radius ** 2 * py_value

    def perimeter(self):
        """Return the perimeter."""
        py_value = math.pi
        return self.radius * 2 * py_value


class Rectangle(Shape):
    """A shape subclass representing a rectangle."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width ensuring it is non-negative."""
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value

    @property
    def height(self):
        """Return the height."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height ensuring it is non-negative."""
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    def area(self):
        """Return the area."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter."""
        return (self.height + self.width) * 2


def shape_info(shape):
    """Print the area and perimeter."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
