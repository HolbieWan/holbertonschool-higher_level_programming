#!/usr/bin/python3
"""Append_write Module"""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8) and returns the number of characters written."""
    with open(filename, mode="a", encoding="utf-8") as file:
        nb_chars = file.write(text)
    return nb_chars
