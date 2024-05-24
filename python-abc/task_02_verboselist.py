#!/usr/bin/python3
"""VerboseList Module"""


class VerboseList(list):
    """A list that prints notifications for item additions and removals."""

    def append(self, item):
        """Add an item to the end of the list."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable."""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """Remove the first occurrence of the item from the list."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        """Remove and return the item at the given position
        or the last item if no index is specified."""
        if index is None:
            item = super().pop()
            print("Popped [{}] from the list.".format(item))
            return item
        else:
            item = super().pop(index)
            print("Popped [{}] from the list.".format(item))
            return item
