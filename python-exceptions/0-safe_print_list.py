#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb_printed = 0
    try:
        for item in my_list[:x]:
            print("{}".format(item), end="")
            nb_printed += 1
        print()

    except TypeError:
        pass

    except IndexError:
        pass

    finally:
        return nb_printed
