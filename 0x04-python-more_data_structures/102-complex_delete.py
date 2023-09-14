#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for mem1, mem2 in a_dictionary.items():
        if mem2 == value:
            new.append(mem1)

    for mem in new:
        del (a_dictionary[mem])
    return a_dictionary
