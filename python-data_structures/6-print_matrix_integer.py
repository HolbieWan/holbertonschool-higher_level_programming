#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for inner_list in matrix:
        for element in inner_list:
            print("{:d}" .format(element), end="")
        print()
