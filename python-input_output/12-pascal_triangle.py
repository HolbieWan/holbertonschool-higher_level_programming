#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return

    pascal_triangle = [[1]]

    for i in range(1, n):
        new_row = [1]
        
        for j in range(1, i):

            new_value = pascal_triangle[i - 1][j - 1]
            + pascal_triangle[i - 1][j]

            new_row.append(new_value)
        new_row.append(1)
        pascal_triangle.append(new_row)

    return (pascal_triangle)
