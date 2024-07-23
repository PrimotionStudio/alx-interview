#!/usr/bin/python3
"""
method that determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding
    """
    isValid = True
    _bin = [bin(i)[2:].zfill(8) for i in data]
    i = 0
    while i < len(_bin):
        byte = _bin[i]
        if byte[0] == '0':
            rest = byte[1:]
        elif byte[0:2] == '10':
            isValid = False
        elif byte[0:3] == '110':
            j = 0
            err = 0
            code_points = ''
            while i < 2:
                _byte = _bin[i]
                if j == 0:
                    code_points += _byte[3:]
                else:
                    if _byte[0:2] == '10':
                        code_points += _byte[2:]
                    else:
                        err = 1
                        isValid = False
                        break
                j = 1
                i += 1
            i += 1
            j = 0
        elif byte[0:4] == '1110':
            j = 0
            err = 0
            code_points = ''
            while i < 3:
                _byte = _bin[i]
                if j == 0:
                    code_points += _byte[4:]
                else:
                    if _byte[0:2] == '10':
                        code_points += _byte[2:]
                    else:
                        err = 1
                        isValid = False
                        break
                j = 1
                i += 1
            i += 2
            j = 0
        elif byte[0:5] == '11110':
            j = 0
            err = 0
            code_points = ''
            while i < 4:
                _byte = _bin[i]
                if j == 0:
                    code_points += _byte[5:]
                else:
                    if _byte[0:2] == '10':
                        code_points += _byte[2:]
                    else:
                        err = 1
                        isValid = False
                        break
                j = 1
                i += 1
            i += 3
            j = 0
        else:
            pass
        i += 1
    return isValid
