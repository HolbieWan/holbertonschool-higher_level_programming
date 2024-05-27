#!/usr/bin/python3
"""Append_write Module"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure) represented by a JSON string:"""
    obj = json.loads(my_str)
    return obj
