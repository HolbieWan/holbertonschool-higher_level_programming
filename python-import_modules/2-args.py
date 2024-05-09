#!/usr/bin/python3
import sys


def print_arguments(*args):

    num_arguments = len(args)
    if num_arguments == 0:
        print("{} argument." .format(num_arguments))
    else:
        print("{} arguments:" .format(num_arguments))
    for i in range(1, num_arguments):
        print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    print_arguments(*sys.argv[1:])
