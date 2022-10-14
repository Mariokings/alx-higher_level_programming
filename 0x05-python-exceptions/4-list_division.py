#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    kc = len(my_list_2)
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except TypeError:
            result = 0
            print("wrong type")
        except ValueError:
            result = 0
        except ZeroDivisionError as div:
            result = 0
            print(div)
        except IndexError:
            result = 0
            print("out of range")
            break
        finally:
            if x > kc - 1:
                break
            else:
                my_list.append(result)
    return my_list
