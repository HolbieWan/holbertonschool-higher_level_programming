#!/usr/bin/python3
"""Class Rectangle"""

class Rectangle:
    """Represent a rectangle with a name"""

    lenght = 0
    height = 0

    count = 0

    def __init__(self, name):
        self.name = name

        Rectangle.count += 1

