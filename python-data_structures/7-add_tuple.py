#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple_a = list(tuple_a[:2])
    new_tuple_b = list(tuple_b[:2])

    new_tuple_a += [0] * (2 - len(new_tuple_a))
    new_tuple_b += [0] * (2 - len(new_tuple_b))

    combined_tuple = (new_tuple_a[0] + new_tuple_b[0],
                      new_tuple_a[1] + new_tuple_b[1])

    return combined_tuple
