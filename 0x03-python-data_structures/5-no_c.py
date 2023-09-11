#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for mem in my_string:
        if mem != "c" and mem != "C":
            new += mem
    return new
