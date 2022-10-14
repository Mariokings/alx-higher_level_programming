#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
            my_list.append(result)
        except TypeError:
            print("wrong type")
            my_list.append(0)
        except ValueError:
            my_list.append(0)
        except ZeroDivisionError as div:
            print(div)
            my_list.append(0)
        except IndexError:
            my_list.append(0)
            print("out of range")
            break
    return my_list
