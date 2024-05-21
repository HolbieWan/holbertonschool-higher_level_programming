#!/usr/bin/python3
"""Print_square"""


def print_square(size):
    """Function that prints a square with the char # """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print("")
