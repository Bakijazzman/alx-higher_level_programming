#!/usr/bin/python3


def multiple_returns(sentence):
    Tuple = ()
    if len(sentence) == 0:
        Tuple = 0, None
    else:
        length = len(sentence)
        Tuple = length,sentence[0]
    return Tuple
