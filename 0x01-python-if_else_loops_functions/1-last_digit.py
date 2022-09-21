#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mark = number
if number < 0:
    number *= -1
if (number > 9) and (number < 100):
    number %= 10
if (number > 99) and (number < 1000):
    number %= 100
    number %= 10
if (number > 999) and (number < 10000):
    number %= 1000
    number %= 100
    number %= 10
if (number > 9999) and (number < 100000):
    number %= 10000
    number %= 1000
    number %= 100
    number %= 10
if number > 5:
    print("Last digit of {} is {} and is greater than 5".format(mark, number))
if number == 0:
    print("Last digit of {} is {} and is 0".format(mark, number))
if (number < 6) and (number != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(mark, number))
