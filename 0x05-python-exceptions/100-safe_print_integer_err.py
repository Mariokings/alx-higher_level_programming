#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except TypeError as ty:
        print("Exception: ", ty)
        return False
    except ValueError as va:
        print("Exception: ", va)
        return False
    else:
        return True
