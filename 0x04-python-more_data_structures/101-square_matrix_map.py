#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    mario = []
    for i in matrix:
        mario.append(list(map(lambda x: x*x, i)))
    return mario
