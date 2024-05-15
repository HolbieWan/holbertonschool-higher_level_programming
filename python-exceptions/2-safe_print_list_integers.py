#!/ussr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nb_printed = 0
    try:
        for item in my_list[:x]:
            if type(item) != int:
                continue
            print("{:d}".format(item), end="")
            nb_printed += 1
        print()

    except (TypeError, IndexError):
        pass

    finally:
        return nb_printed
