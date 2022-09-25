def element_at(my_list, idx):
    if idx < 0:
        return None
    mario = len(my_list) - 1
    if idx > mario:
        return None
    kc = my_list.pop(idx)
    return kc
