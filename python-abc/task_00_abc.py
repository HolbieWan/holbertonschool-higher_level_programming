#!/usr/bin/python3
"""Abstract classes"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Class animal"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Animal Subclass Dog"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Animal Subclass Cat"""

    def sound(self):
        return "Meow"
