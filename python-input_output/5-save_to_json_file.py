#!/usr/bin/python3
"""save_to_json_file Module"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    new_json_string = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8")\
    as file:
        return file.write(new_json_string)
