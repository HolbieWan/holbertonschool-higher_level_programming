#!/usr/bin/python3

def pascal_triangle(n: int = 1):

    pascal_list = [[1]]

    for i in range(1, n):
        new_list = [1]
        for j in range(1, i):
            new_value = pascal_list[i - 1][j - 1] + pascal_list[i -1][j]
            new_list.append(new_value)

        new_list.append(1)
        pascal_list.append(new_list)

    for list in pascal_list:
        print(list)

pascal_triangle(10)