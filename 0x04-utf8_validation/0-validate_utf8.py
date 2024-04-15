#!/usr/bin/python3
"""UTF-8 validation module.

This module provides a function, validUTF8, to check if a list of integers
represents valid UTF-8 codepoints according to the UTF-8 encoding rules.

"""


def validUTF8(data):
    """Checks if a list of integers represents valid UTF-8 codepoints.

    Args:
        data (list of int): List of integers representing UTF-8 codepoints.

    Returns:
        bool: True if the list represents valid UTF-8 codepoints, False
        otherwise.
    """
    s = 0
    n = len(data)
    for i in range(n):
        if s > 0:
            s -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            s = 0
        elif data[i] & 0b11111000 == 0b11110000:
            p = 4
            if n - i >= p:
                nb = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + p],
                ))
                if not all(nb):
                    return False
                s = p - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            p = 3
            if n - i >= p:
                nb = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + p],
                ))
                if not all(nb):
                    return False
                s = p - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            p = 2
            if n - i >= p:
                nb = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + p],
                ))
                if not all(nb):
                    return False
                s = p - 1
            else:
                return False
        else:
            return False
    return True
