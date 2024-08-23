#!/usr/bin/python3
"""
a solution to the making change problem
"""
import sys


change = []


def makeChange(coins, total):
    """a function to make change
    first make sure list is sorted to
    ensure the biggest value is at the end
    """
    sys.setrecursionlimit(9999999)
    if total <= 0:
        return 0
    if not any([True for x in coins if x <= total]):
        return -1
    coins.sort()
    t = recursive(coins, total)
    if t == 0:
        return len(change)
    else:
        return -1


def recursive(coins, total):
    """recursion to make change"""
    if total == 0:
        return total
    if total <= 0:
        return -1
    # trim coins if necessary
    coins = [x for x in coins if x <= total]
    if len(coins) == 0:
        return -1
    total -= coins[-1]
    change.append(coins[-1])
    return recursive(coins, total)
