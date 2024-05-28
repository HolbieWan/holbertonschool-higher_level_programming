#!/usr/bin/python3
"""Basic pickle Module"""
import pickle


class CustomObject:
    """Class CustomObject"""
    name = ""
    age = 0
    is_student = True

    def __init__(self, name, age, is_student):
        """Method to initialize a new instance of an object
        of class CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Method that displays the attributes of a CustomObject"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is_student: {}".format(self.is_student))

    def serialize(self, filename):
        """Function to serialize a Python object to a pickle file"""
        try:
            with open(filename, 'wb') as file:
                My_serialized_pickle = pickle.dump(self, file)
                return My_serialized_pickle
        except (pickle.PicklingError) as e:
            print("Serialization error: {}".format(e))
            return None

    @classmethod
    def deserialize(cls, filename):
        """Function to deserialize a pickle file to a Python object"""
        try:
            with open(filename, 'rb') as file:
                My_deserialized_pickle = pickle.load(file)
            return My_deserialized_pickle
        except (pickle.UnpicklingError) as e:
            print("Deserialization error: {}".format(e))
            return None
