#!/usr/bin/python3
"""Import Module here """


def append_write(filename="", text=""):
    """Appends to a file and creates if it doesnt exist"""
    with open(filename, 'a', encoding="utf-8") as files:
        count = len(text)
        files.write(text)
        return count
