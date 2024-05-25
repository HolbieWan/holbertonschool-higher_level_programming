#!/usr/bin/python3

class SwimMixin:
    """Mixin class to provide swimming capability."""

    def swim(self):
        """Prints a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to provide flying capability."""

    def fly(self):
        """Prints a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon with both swimming and flying capabilities."""

    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")
