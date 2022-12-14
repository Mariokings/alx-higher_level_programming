#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as ty:
        print("Exception: ", ty)
        return False
    except ValueError as va:
        print("Exception: ", va)
        return False
    except NameError as na:
        print("Exception: ", na)
        return False
