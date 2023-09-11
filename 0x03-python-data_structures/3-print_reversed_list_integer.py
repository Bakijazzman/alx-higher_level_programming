#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    length = len(my_list)
    for n in range(length):
        print("{}".format(my_list[n]))
