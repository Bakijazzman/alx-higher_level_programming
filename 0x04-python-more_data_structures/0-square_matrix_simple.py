#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    if len(matrix) == 0:
        return matrix
    for row in matrix:
        _new_ = []
        for mem in row:
            _new_.append(mem * mem)
        new.append(_new_)
    return new
