#!/usr/bin/python3
for alpha in range(25, -1, -1):
    char = alpha + 65
    if alpha % 2 == 1:
        char += 32
    print("{:c}".format(char), end="")
