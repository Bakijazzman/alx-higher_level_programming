#!/usr/bin/python3
"""Import Module Here """


def read_file(filename=""):
    """opens a file for reading"""
    with open(filename, 'r', encoding="UTF-8") as files:
        Read = files.read()
        print(Read, end="")
