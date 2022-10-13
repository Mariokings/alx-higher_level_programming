#!/usr/bin/python3

def safe_print_division(a, b):
    count = 0
    try:
        result = a / b
    except ZeroDivisionError:
        count += 1
    finally:
        if count == 1:
            print("Inside result: {}".format(None))
            return None
        else:
            print("Inside result: {}".format(result))
            return result
