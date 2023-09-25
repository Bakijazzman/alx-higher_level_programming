#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for mem in range(x):
            print(my_list[mem], end="")
            count += 1
    except (TypeError, ValueError):
        pass
    print()
    return count
