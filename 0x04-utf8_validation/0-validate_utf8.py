#!/usr/bin/python3
"""
method that determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding

    RULES:
    0 - 1 byte of UTF-8
    110 - 2 byte of UTF-8
    1110 - 3 byte of UTF-8
    11110 - 4 byte of UTF-8

    10 - 2nd, 3rd or 4th byte of the immediate above 3
    (110, 1110, 11110)
    """
    _bin = [bin(i)[2:].zfill(8) for i in data]
    i = 0
    while i < len(_bin):
        byte = _bin[i]
        if byte[0] == '0':
            # Matches with ASCII
            print("Matches with ASCII")
            # pass
        elif byte[0:2] == '110':
            # Contains 2 bytes code points
            print("Contains 2 bytes code points")
            pass
        elif byte[0:3] == '1110':
            # Contains 3 bytes code points
            print("Contains 3 bytes code points")
            pass
        elif byte[0:4] == '11110':
            # Contains 4 bytes code points
            print("Contains 4 bytes code points")
            pass
        elif byte[0:1] == '10':
            # 2nd, 3rd or 4th byte of the immediate above 3
            print("2nd, 3rd or 4th byte of the immediate above 3 (110, 1110, 11110)")
            # (110, 1110, 11110)
            pass
        i += 1
    print(_bin)
    return True