"""
This module checks if a number is prime
"""
from sys import argv
from typing import List, Tuple, Optional


def returnPrimeFactors(i: int, n: int) -> Optional[List[int]]:
    """
    Returns a list of prime factors of a number
    """
    if isPrimeNumber(n):
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

print(genPrimeFactors(int(argv[1])))