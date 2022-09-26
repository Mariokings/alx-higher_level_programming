#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)

    if (a == 0):
        mario = (a, None)
    else:
        mario = (a, sentence[0])

    return (mario)
