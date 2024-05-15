#!/usr/bin/python3
"""Prime game module.

This module provides a function to determine the winner of a prime game
session.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
    x (int): The number of rounds.
    nums (list of int): A list of `x` integers representing
    the limit for each round.

    Returns:
    str or None: The name of the player that won the most rounds.
                 If the winner cannot be determined, returns None.
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, limit in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: limit])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
