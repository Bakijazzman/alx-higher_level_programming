#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    sum = 0
    for mem in new:
        sum += mem
    return sum
