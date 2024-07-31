#!/usr/bin/python3
"""0-nqueens.py"""
from sys import argv, exit
from pprint import pprint


def nqueens(n: int):
    """
    Return a list of all possible positions
    of queens on an NxN chessboard
    such that no two queens attack each other.
    """
    col = [-1 for i in range(n)]
    row = [-1 for i in range(n)]
    posDiag = []
    negDiag = []
    for r in range(n):
        print("[", end="")
        no_bt = 0
        for c in range(n):
            nD = r - c  # negative diagonal
            pD = r + c  # positive diagonal
            if r in row:
                x = c  # because one column has already been taken away from the row
                # a queen is already on this row
                # means go to the next row, but complete this
                # board visualization first
                while x < n:
                    print(" (.,.) |", end="")
                    x += 1
                print("# r is in row", end="")
                r += 1
                break
            if c in col:
                print(" (.,.) #c in col |", end="")
                continue
            if pD in posDiag:
                print(" (.,.) #pD in posDiag |", end="")
                continue
            if nD in negDiag:
                print(" (.,.) #nD in negDiag |", end="")
                continue
            # if r not in row and c not in col and nD not in negDiag and pD not in posDiag:
                # print(r, "is not in", row)
                # print(r, "is not in", col)
            print(f" ({r},{c}) |", end="")
            row[r] = r
            col[c] = c
            negDiag.append(nD)
            posDiag.append(pD)
            no_bt = 1
        print("]", end="\n\n")
    print("row")
    pprint(row)
    print("-----------------------------------")
    print("col")
    pprint(col)
    print("-----------------------------------")
    print("negDiag")
    pprint(negDiag)
    print("-----------------------------------")
    print("posDiag")
    pprint(posDiag)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
        if n < 4:
            print("N must be atleast 4")
            exit(1)

        nqueens(n)  # main event function

    except ValueError:
        print("N must be an integer")
        exit(1)
