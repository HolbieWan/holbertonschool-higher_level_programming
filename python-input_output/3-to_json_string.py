#!/usr/bin/python3
"""Append_write Module"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    new_json_string = json.dumps(my_obj)
    return new_json_string
