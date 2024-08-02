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
    col = []
    row = []
    posDiag = []
    negDiag = []
    state = []
    backtrack = -1
    end_of_loop_but_bt = 0
    new_r = new_c = None

    def _backtrack():
        c = state[-1]["col"]
        if c == n - 1:
            col.pop()
            row.pop()
            posDiag.pop()
            negDiag.pop()
            state.pop()
            return _backtrack()
        r = state[-1]["row"]
        if r == n - 1:
            col.pop()
            row.pop()
            posDiag.pop()
            negDiag.pop()
            state.pop()
            return _backtrack()
        col.pop()
        row.pop()
        posDiag.pop()
        negDiag.pop()
        state.pop()
        return (r, c + 1)

    r = 0
    while r < n or end_of_loop_but_bt == 1:
        if end_of_loop_but_bt == 1:
            end_of_loop_but_bt = 0
        if backtrack == 1:
            new_r, new_c = _backtrack()

        backtrack = 1  # 1 means backtracking may be needed
        if new_r:
            r = new_r
            new_r = None
        if state == []:
            r = 0
        if r in row:
            continue
        c = 0
        if new_c:
            c = new_c
            new_c = None
        while c < n:
            if c in col:
                c += 1
                continue
            nD = r - c
            pD = r + c
            if nD in negDiag:
                c += 1
                continue
            if pD in posDiag:
                c += 1
                continue
            col.append(c)
            row.append(r)
            negDiag.append(nD)
            posDiag.append(pD)
            state_obj = {
                "row": r,
                "col": c,
            }
            state.append(state_obj)
            backtrack = -1  # -1 means no need for backtracking
            break
        if backtrack == 1 and r == n - 1:
            end_of_loop_but_bt = 1
        r += 1

    print([[_["row"], _["col"]] for _ in state])
    print([[_["col"], _["row"]] for _ in state])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)

        nqueens(n)  # main event function

    except ValueError:
        print("N must be a number")
        exit(1)
