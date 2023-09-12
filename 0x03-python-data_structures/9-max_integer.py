#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        new = my_list.copy()
        new.sort()
        return new[len(new) - 1]
