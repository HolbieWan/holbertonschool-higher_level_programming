#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    total = 0
    i = 0

    while i < len(roman_string):
        value = roman_dict[roman_string[i]]

        if i + 1 < len(roman_string) and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            total -= value
        else:
            total += value

        i += 1

    return total
