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
    # col = [-1 for i in range(n)]
    # row = [-1 for i in range(n)]
    col = []
    row = []
    posDiag = []
    negDiag = []
    backtrack = -1
    state = []
    new_r = None
    new_c = None
    end_of_loop_but_bt = 0

    def _backtrack():
        print("beginning of backtracking function")
        # try:
        c = state[-1]["col"]
        print("is", c, "==", n, "- 1")
        if c == n - 1:
            print("yes")
            col.pop()
            row.pop()
            posDiag.pop()
            negDiag.pop()
            state.pop()
            return _backtrack()
        print("no")
        r = state[-1]["row"]
        print("is", r, "==", n, "- 1")
        if r == n - 1:
            print("yes")
            col.pop()
            row.pop()
            posDiag.pop()
            negDiag.pop()
            state.pop()
            return _backtrack()
        print("no")
        col.pop()
        row.pop()
        posDiag.pop()
        negDiag.pop()
        state.pop()
        # except IndexError:
        #     c = 0
        #     r = 0
        return (r, c + 1)

    r = 0
    while r < n or end_of_loop_but_bt == 1:
        if end_of_loop_but_bt == 1:
            end_of_loop_but_bt = 0
            print("Backtracking at the end of the loop")
        if backtrack == 1:
            print("Need for backtracking")
            # to backtrack, i need to remove the last element i added, and reset my counter to the value it was (before i added the last element) plus 1 (+1) (before i added the last element) so that it will skip the position of the last element and go to the next
            print("state before backtracking")
            pprint(state)
            new_r, new_c = _backtrack()
            print("state after backtracking")
            pprint(state)

        backtrack = 1  # 1 means backtracking may be needed
        if new_r:
            r = new_r
            new_r = None
        if state == []:
            r = 0
        print("Current ROW:", r)

        print("Decision Point for Row")
        if r in row:
            print(r, "already in", row)
            continue
        # row r is currently free

        # for c in range(n):
        c = 0
        if new_c:
            c = new_c
            new_c = None
        while c < n:
            print("Current Column", c)
            print("Decision Point for Col")
            if c in col:
                print(c, "already in", col)
                c += 1
                continue
            # col c is currently free

            nD = r - c
            pD = r + c
            print("Decision Point for negDiag")
            if nD in negDiag:
                print(nD, "already in", negDiag)
                c += 1
                continue
            # negDiag is currently safe

            print("Decision Point for posDiag")
            if pD in posDiag:
                print(pD, "already in", posDiag)
                c += 1
                continue
            # posDiag is currently safe

            print(f"Adding to col: {c}, row: {r}, negDiag: {nD}, posDiag: {pD}")
            board = [(-1, -1)] * n
            board[c] = (r, c)
            pprint(board)

            # col[c] = c
            # row[r] = r
            col.append(c)
            row.append(r)
            negDiag.append(nD)
            posDiag.append(pD)
            # append to state, to show the changes made
            state_obj = {
                "row": r,
                "col": c,
            }
            state.append(state_obj)
            backtrack = -1  # -1 means no need for backtracking
            break

        print("Backtrack:", backtrack)
        if backtrack == 1 and r == n - 1:
            # something to hep and backtrack
            end_of_loop_but_bt = 1
        r += 1

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
