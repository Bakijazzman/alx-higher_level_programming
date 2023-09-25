#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        for mem in range(x):
            print(my_list[mem], end="")
            index += 1
    except IndexError:
        pass
    print()
    return index
