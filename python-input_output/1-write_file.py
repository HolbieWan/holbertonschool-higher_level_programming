#!/usr/bin/python3
"""write_file Module"""


def write_file(filename="", text=""):
    """Function that overrides the string: text
    and returns the number of added char"""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
