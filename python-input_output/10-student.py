#!/usr/bin/python3
"""9-student Module"""


class Student:
    """Class that defines a student"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Method to initialize a Student instanciation"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Method to returns the dictionary description
        for JSON serialization of an objec"""

        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            is_valid = True
            for attr in attrs:
                if not isinstance(attr, str):
                    is_valid = False
                    break

            if is_valid:
                result = {}
                for attr in attrs:
                    if attr in self.__dict__:
                        result[attr] = self.__dict__[attr]
                return result

        return self.__dict__
