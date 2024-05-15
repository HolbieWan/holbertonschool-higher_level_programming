#!/ussr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nb_printed = 0
    for item in my_list[:x]:
        try:
            print("{:d}".format(item), end="")
            nb_printed += 1

        except (ValueError, TypeError):
            continue
    print()

    return nb_printed
