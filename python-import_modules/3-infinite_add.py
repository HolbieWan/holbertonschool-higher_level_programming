#!/usr/bin/python3
import sys


def add_arguments(*args):

    num_arguments = len(args)
    sum_args = 0

    if num_arguments == 0:
        print("{}".format(num_arguments))

    else:

        for i in range(0, num_arguments):
            sum_args += int(args[i])

        print("{}".format(sum_args))


if __name__ == "__main__":
    add_arguments(*sys.argv[1:])
