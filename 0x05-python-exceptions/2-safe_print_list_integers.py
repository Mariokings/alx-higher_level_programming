#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for y in x:
        try:
            print("{d}".format(my_list[y), end="")
            count += 1
        except ValueError:
            continue
        except IndexError:
            break
    print()
    return count
