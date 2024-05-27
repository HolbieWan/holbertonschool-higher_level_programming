#!/usr/bin/python3
"""Read_file """


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as file:
        read = file.read()
        print(read, end="")
