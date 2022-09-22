#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    for i in str:
        if index != n:
            alphabet = i
        index += 1
