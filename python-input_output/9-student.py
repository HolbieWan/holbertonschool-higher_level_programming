#!/usr/bin/python3
"""9-student Module"""


class Student:
    """Class that defines a student"""
    first_name = ""
    last_name = ""
    age = 0
    
    def __init__(self, first_name, last_name, age):
        """Method to initialize a Student instanciation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to returns the dictionary description
        for JSON serialization of an objec"""
        return self.__dict__
