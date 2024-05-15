#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb_printed = 0
    try:
        for item in my_list[:x]:
            print("{}".format(item), end="")
            nb_printed += 1
        print()

    except TypeError as e:
        print("An error occurred:", e)

    except IndexError:
        print("Index out of range.")

    finally:
        return nb_printed
