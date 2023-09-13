def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for mem in new:
        new[mem] *= 2
    return new
