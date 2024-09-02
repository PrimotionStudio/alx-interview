#!/usr/bin/python3
"""Precompute primes and Grundy numbers"""


def isWinner(x, nums):
    MAX_N = 10000
    is_prime = [True] * (MAX_N + 1)
    primes = []

    is_prime[0] = is_prime[1] = False
    for num in range(2, MAX_N + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, MAX_N + 1, num):
                is_prime[multiple] = False

    grundy = [0] * (MAX_N + 1)

    for n in range(2, MAX_N + 1):
        reachable = set()
        for prime in primes:
            if prime > n:
                break
            for multiple in range(prime, n + 1, prime):
                reachable.add(grundy[n - multiple])
        # Calculate the minimum excludant (mex)
        mex = 0
        while mex in reachable:
            mex += 1
        grundy[n] = mex

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if grundy[n] != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
