#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for mem in range(list_length):
        result = 0
        try:
            result = my_list_1[mem] / my_list_2[mem]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(result)
    return new_list
