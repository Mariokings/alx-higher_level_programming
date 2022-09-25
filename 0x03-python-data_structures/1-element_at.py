def element_at(my_list, idx):
    if idx < 0:
        return
    mario = len(my_list) - 1
    if idx > mario:
        return
    kc = my_list[idx]
    return kc
