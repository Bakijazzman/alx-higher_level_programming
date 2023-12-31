#!/usr/bin/python3
"""
This module contains a function that indents texts
"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"
    Args:
        text (str): The string to be printed
    Raises:
        TypeError: If text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == " ":
        i = i + 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i = i + 1
            while i < len(text) and text[i] == " ":
                i = i + 1
            continue
        i = i + 1
