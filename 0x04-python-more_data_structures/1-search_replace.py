#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mario = []
    for i in my_list:
        if i == search:
            mario.append(replace)
        else:
            mario.append(i)
    return mario
