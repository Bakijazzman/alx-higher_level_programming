#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        total = add(a, b)
        for idx in range(4, 6):
            total = add(total, idx)
        return total
    else:
        return sub(a, b)
