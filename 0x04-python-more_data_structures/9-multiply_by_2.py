#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    kc = a_dictionary.copy()
    for i in kc:
        kc[i] = kc[i] * 2
    return kc
