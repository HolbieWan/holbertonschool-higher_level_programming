#!/usr/bin/pythons3
"""'1-my_list' module"""


class MyList(list):
    """Method that prints the list, but sorted in ascending order"""

    def print_sorted(self):
        print(sorted(self))
