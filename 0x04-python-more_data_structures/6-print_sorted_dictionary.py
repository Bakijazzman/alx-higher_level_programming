#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for mem in sorted(a_dictionary.keys()):
        print("{} : {}".format(mem, a_dictionary[mem]))
