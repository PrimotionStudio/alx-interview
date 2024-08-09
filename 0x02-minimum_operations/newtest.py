"""
This module checks if a number is prime
"""
from sys import argv
from typing import List, Tuple, Optional


prime_numbers = []


def genPrimeFactors(possible_prime, n: int) -> List[int]:
    """
    This function divides n and append the possible prime
    prime_numbers
    """
    while possible_prime <= n:
        if isPrimeNumber(possible_prime) and n % possible_prime == 0:
            prime_numbers.append(possible_prime)
            new_num = n / possible_prime
            genPrimeFactors(possible_prime, new_num)
            break
        possible_prime += 1


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
    if n <= 1:
        return 0
    genPrimeFactors(2, n)
    return sum(prime_numbers)


print(minOperations(int(argv[1])))
