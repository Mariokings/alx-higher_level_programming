#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        mario = None
    else:
       my_list.sort()
       mario = my_list[-1]
    return mario

