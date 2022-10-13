#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count
