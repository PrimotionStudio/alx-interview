#!/usr/bin/python3
"""
This module contains a function that
returns the minimum number of operation
required to copy and paste a character in a text editor
"""
from typing import List, Tuple, Optional


def returnPrimeFactors(n: int) -> Optional[List[int]]:
    """
    Returns a list of prime factors of a number
    """
    if isPrimeNumber(i):
        if i % n == 0:
            first_num = i
            second_num = n / i
            return [first_num, returnPrimeFactors(second_num)]



def genPrimeFactors(n: int) -> List[int]:
    """
    This function returns a list of prime factors of a number
    """
    factors = []
    i = 2
    while i <= n:
        if isPrimeNumber(i):
            if n % i == 0:
                factors.append(i)
        i += 1
    return(factors)

def isPrimeNumber(n: int) -> bool:
    """
    This function checks if a number is prime
    """
    if n < 1:
        return False
    if n == 1:
        return True
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

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