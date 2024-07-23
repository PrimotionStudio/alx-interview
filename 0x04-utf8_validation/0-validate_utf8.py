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
    isValid = True
    _bin = [bin(i)[2:].zfill(8) for i in data]
    i = 0
    while i < len(_bin):
        print("i is", i)
        # while iterating, `i` must not land on bytes
        # starting with `10` else, it will be considered
        # an error because provisions will be made for bytes
        # starting with `10` when their headding bytes are found
        byte = _bin[i]
        print(byte[0:4])
        if byte[0] == '0':
            # Matches with ASCII
            print("Matches with ASCII")
            rest = byte[1:] # correct ASCII or UTF-8 code
            # pass
        elif byte[0:2] == '10':
            # 2nd, 3rd or 4th byte of the immediate below 3
            print("Not a leading byte, AN ERROR, SKIP!")
            isValid = False
            # (110, 1110, 11110)
            # pass
        elif byte[0:3] == '110':
            # Contains 2 bytes code points
            print("Contains 2 bytes code points")
            # Looping through the 2 bytes and taking
            # the code points and removing its flags
            j = 0
            err = 0 # err flag
            code_points = ''
            while i < 2:
                _byte = _bin[i]
                print("Viewing following bytes", _byte[0:4])
                # Get the heading bytes and remove its flag
                if j == 0:
                    # heading flag
                    code_points += _byte[3:]
                else:
                    # following byte
                    if _byte[0:2] == '10':
                        code_points += _byte[2:]
                    else:
                        # this means that in this case,
                        # the following bytes were not consistent
                        # with `10` and is generating an error
                        err = 1 # set err flag to 1
                        print("the following bytes were not consistent")
                        isValid = False
                        break
                j = 1
                i += 1
            if err == 0:
                # if err flag is not set, then the code points
                # are correct
                print("Correct code points")
            i += 1
            print("sub i is", i)
            j = 0 # reset j just in case
            # pass
        elif byte[0:4] == '1110':
            # Contains 3 bytes code points
            print("Contains 3 bytes code points")
            # Looping through the 3 bytes and taking
            # the code points and removing its flags
            j = 0
            err = 0 # err flag
            code_points = ''
            while i < 3:
                _byte = _bin[i]
                print("Viewing following bytes", _byte[0:4])
                # Get the heading bytes and remove its flag
                if j == 0:
                    # heading flag
                    code_points += _byte[4:]
                else:
                    # following byte
                    if _byte[0:2] == '10':
                        code_points += _byte[2:]
                    else:
                        # this means that in this case,
                        # the following bytes were not consistent
                        # with `10` and is generating an error
                        err = 1 # set err flag to 1
                        print("the following bytes were not consistent")
                        isValid = False
                        break
                j = 1
                i += 1
            if err == 0:
                # if err flag is not set, then the code points
                # are correct
                print("Correct code points")
            i += 2
            print("sub i is", i)
            j = 0 # reset j just in case
            # pass
        elif byte[0:5] == '11110':
            # Contains 4 bytes code points
            print("Contains 4 bytes code points")
            # Looping through the 4 bytes and taking
            # the code points and removing its flags
            j = 0
            err = 0 # err flag
            code_points = ''
            while i < 4:
                _byte = _bin[i]
                print("Viewing following bytes", _byte[0:4])
                # Get the heading bytes and remove its flag
                if j == 0:
                    # heading flag
                    code_points += _byte[5:]
                else:
                    # following byte
                    if _byte[0:2] == '10':
                        code_points += _byte[2:]
                    else:
                        # this means that in this case,
                        # the following bytes were not consistent
                        # with `10` and is generating an error
                        err = 1 # set err flag to 1
                        print("the following bytes were not consistent")
                        isValid = False
                        break
                j = 1
                i += 1
            if err == 0:
                # if err flag is not set, then the code points
                # are correct
                print("Correct code points")
            i += 3
            print("sub i is", i)
            j = 0 # reset j just in case
            # pass
        else:
            # Invalid
            pass
        i += 1
    print(_bin)
    return isValid