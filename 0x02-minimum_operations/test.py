"""
This module checks if a number is prime
"""
from sys import argv
from typing import List, Tuple, Optional

def getOtherNumber(factor: int, n: int) -> Optional[List[int]]:
    """
    Returns the other number in the factor
    """
    if isPrimeNumber(factor):
        if n % factor == 0:
            otherNumber = n / factor
            return [factor, getOtherNumber(otherNumber, n)]
        return[None]
    return[None]


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
    """
    This function returns the minimum number of operations
    required to copy and paste a character in a text editor
    """
    if n == 1:
        return 0
    primeFactors = genPrimeFactors(n)
    operations = []
    for factor in primeFactors:
        operations.extend(getOtherNumber(factor, n))
    print(operations)
    return 1

print(minOperations(int(argv[1])))