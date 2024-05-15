#!/usr/bin/python3

def safe_print_division(a, b):
    div  = 0
    try:
        div = a / b

    except (ZeroDivisionError, TypeError):
        result = None

    finally:
        print("Inside result: {:1f}".format(div))
        return div or None
