#!/usr/bin/pyhton3
"""Read_file Module"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, mode="r", encoding="Utf-8") as file:
        print(file.read())
