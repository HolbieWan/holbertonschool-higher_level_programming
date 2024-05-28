#!/usr/bin/python3
"""Basic Serialization Module"""
import json


def serialize_and_save_to_file(data, filename):
    """Function to serialize a Python dictionary to a JSON file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        obj = json.dump(data, file)
        return obj


def load_and_deserialize(filename):
    """Function to deserialize a JSON file to recreate the Python Dictionary"""
    with open(filename, mode="r", encoding="utf-8") as file:
        recreated_dict = json.load(file)
        return recreated_dict
