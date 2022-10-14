#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except (TypeError, ValueError):
            result = 0
            print("wrong type")
        except ZeroDivisionError as div:
            result = 0
            print(div)
        except IndexError:
            result = 0
            print("out of range")
        finally:
            my_list.append(result)
    return my_list
