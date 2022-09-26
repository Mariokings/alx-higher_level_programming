#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mario = []
    for i in my_list:
        if i % 2 == 0:
            mario.append(True)
        else:
            mario.append(False)
    return mario
