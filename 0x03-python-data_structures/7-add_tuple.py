#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        a = tuple_a[0]
        b = 0
    elif len(tuple_a) == 0:
        a = 0
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]
    
    if len(tuple_b) == 1:
        a1 = tuple_b[0]
        b1 = 0
    elif len(tuple_b) == 0:
        a1 = 0
        b1 = 0
    else:
        a1 = tuple_b[0]
        b1 = tuple_b[1]
    k = a + a1
    c = b + b1
    mario = (k, c)
    return mario
