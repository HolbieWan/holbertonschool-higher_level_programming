#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] = new_dict[key] * 2

    return new_dict

print(multiply_by_2({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}))