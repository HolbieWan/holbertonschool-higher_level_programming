#!/usr/bin/python3
"""Load_from_json Module"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as file:
        obj = json.load(file)
        return obj
