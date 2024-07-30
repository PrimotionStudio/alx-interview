#!/usr/bin/python3
"""0-nqueens.py"""
from sys import argv, exit

def nqueens(n: int):
    """
    Return a list of all possible positions
    of queens on an NxN chessboard
    such that no two queens attack each other.
    """

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
        if n < 4:
            print("N must be atleast 4")
            exit(1)

        nqueens(n) # main event function

    except ValueError:
        print("N must be an integer")
        exit(1)
