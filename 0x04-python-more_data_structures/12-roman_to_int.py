#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    i, v, x, k, c, d, m = 1, 5, 10, 50, 100, 500, 1000
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
