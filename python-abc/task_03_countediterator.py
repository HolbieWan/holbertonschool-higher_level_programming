#!/usr/bin/python3
"""CountedIterator Module"""


class CountedIterator:
    """Iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the current count of items iterated over."""
        return self.counter
