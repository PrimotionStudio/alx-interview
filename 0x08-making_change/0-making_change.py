#!/usr/bin/python3
"""
A more optimal solution to the making change problem.
"""


def makeChange(coins, total):
    """
    Function to determine the minimum number
    of coins needed to make change.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        if coin <= total:
            count += total // coin
            total %= coin
    return count if total == 0 else -1
