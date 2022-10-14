#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as ty:
        import sys
        print("Exception: {}".format(ty), file=sys.stderr)
        return False
