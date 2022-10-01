#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    i = 1
    v = 5
    x = 10
    k = 50
    c = 100
    d = 500
    m = 1000
    count = mario = check = 0
    for q in roman_string:
        if q == "I":
            num = i
        elif q == "V":
            num = v
        elif q == "X":
            num = x
        elif q == "L":
            num = k
        elif q == "C":
            num = c
        elif q == "D":
            num = d
        else:
            num = m
        if count >= 1 and check < num:
            kc = num - check - check
            check = num
            count += 1
            mario += kc
            continue
        count += 1
        check = num
        mario += num
    return mario
