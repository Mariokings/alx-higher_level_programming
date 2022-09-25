#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mario = []
    for i in my_list:
        if my_list.index(i) == idx:
            mario.append(element)
        else:
            mario.append(i)
    return mario
