#!/usr/bin/pyhton3
"""Read_file """


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, mode="r", encoding="utf-8") as file:
        read_file = file.read()
        print(read_file, end="")
