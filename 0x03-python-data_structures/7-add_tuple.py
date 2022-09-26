#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 1:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + 0
        mario = (a, b)
    elif len(tuple_b) == 0:
        a = tuple_a[0] + 0
        b = tuple_a[1] + 0
        mario = (a, b)
    else:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
        mario = (a, b)
    return mario
