#!/usr/bin/python3

def max_integer(my_list=[]):
    max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
        
    return max

print(max_integer([1, 2, 8, 4, 5]))