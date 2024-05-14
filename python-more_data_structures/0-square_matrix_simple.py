#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        new_list = []

        for x in i:
            new_list.append(x ** 2)

        new_matrix.append(new_list)
        
    return new_matrix
