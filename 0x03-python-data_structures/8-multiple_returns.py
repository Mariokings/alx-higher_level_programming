#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0]

    if a == 0:
        mario = (a, None)
    else:
        mario = (a, b)
    return (mario)
