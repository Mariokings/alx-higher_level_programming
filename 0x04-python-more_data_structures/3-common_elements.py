#!/usr/bin/python3
def common_elements(set_1, set_2):
    kc = [x for i in set_1 for x in set_2 if i == x]
    return kc
