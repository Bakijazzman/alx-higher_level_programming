#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for mem1, mem2 in new.items():
        new[mem1] = mem2 * 2
    return new
