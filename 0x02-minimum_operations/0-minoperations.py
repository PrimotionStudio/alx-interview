#!/usr/bin/python3
"""
This module contains a function that
returns the minimum number of operation
required to copy and paste a character in a text editor
"""
from typing import List, Tuple


def minOperations(n: int) -> int:
    arr: List[Tuple[int]] = []
    i: int = 2
    while i < n / 2:
        if i % n == 0:
            arr.append((i, n).abs(i - (n / i)))
    if len(arr) == 0:
        return n
    sorted(arr)
    return arr[0][0] + arr[0][1]