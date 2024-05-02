#!/usr/bin/python3
"""Module for making change.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    total amount, given a pile of coins with different values.

    Args:
        coins (list): A list of coin values.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
            Returns -1 if the total cannot be met by any combination
            of coins.
    """
    if total <= 0:
        return 0

    remaining = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining > 0:
        if coin_index >= num_coins:
            return -1

        if remaining - sorted_coins[coin_index] >= 0:
            remaining -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count
