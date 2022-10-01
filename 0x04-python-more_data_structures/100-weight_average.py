#!/usr/bin/python3
def weight_average(my_list=[]):
    count = 1
    idx = 0
    kc = 0
    mario = 0
    for i in my_list:
        for x in i:
            count *= x
            idx += 1
            if idx == 2:
                kc += x
        mario += count
        idx = 0
        count = 1
    return float(mario) / kc
