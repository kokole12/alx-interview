#!/usr/bin/python3
"""
    Implementing utf-8 validation in python
    walk through
        Traverse the given array
        Find the number of bytes for each
        Check if the next n-1 start with 10, if not return false
        Finally return true
"""


def validUTF8(data):
    """assiging the initial value of bytes"""
    number_bytes = 0

    """traversing the array"""
    if number_bytes == 0:
        for val in data:
            if val >> 7 == 0b0:
                continue
            elif val >> 5 == 0b110:
                number_bytes = 1
            elif val >> 4 == 0b1110:
                number_bytes = 2
            elif val >> 3 == 0b11110:
                number_bytes = 3
            else:
                return False
    else:
        """checking if element at n-1 starts with 0b10"""
        if val >> 6 != 0b10:
            return False
        number_bytes -= 1

    return number_bytes == 0
