#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for r in matrix:
        if len(r) == 0:
            print()
        for c in range(len(r)):
            print("{:d}".format(r[c]), end="")
            if c == len(r) - 1:
                print()
            else:
                print(" ", end="")
