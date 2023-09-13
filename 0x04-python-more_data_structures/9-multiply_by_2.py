def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for mem in new:
        new[mem] *= 2
    return new
