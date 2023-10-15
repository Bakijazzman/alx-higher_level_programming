#!/usr/bin/python3
"""Import Module here"""


def write_file(filename="", text=""):
    """erite a text to a file """
    with open(filename, 'w', encoding="utf-8") as files:
        return files.write(text)
