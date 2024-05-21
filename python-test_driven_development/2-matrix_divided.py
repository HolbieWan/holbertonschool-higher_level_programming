#!/usr/bin/python3
"""Module that divides a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if (matrix == [] or matrix == [[]] or
        type(matrix) is not list or
            not all(type(row) is list for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
