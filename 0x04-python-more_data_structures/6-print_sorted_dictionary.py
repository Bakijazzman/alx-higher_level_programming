#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary)
    for mem in new:
        print(f"{mem} : {a_dictionary[mem]}")
