#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    remainder = total  # keep track of remainder
    sorted_coins = coins[:]
    sorted_coins.sort(reverse=True)  # take coins in descending order
    count = 0
    # print(sorted_coins)
    if total <= 0:  # 0 as total gets 0
        return 0
    idx_track = 0  # track current index
    while (remainder > 0):
        try:
            # ensure total isn't exceeded
            if remainder - sorted_coins[idx_track] >= 0:
                remainder -= sorted_coins[idx_track]
                count += 1  # increment
            else:  # if it exceeds, do not add; move to next index
                idx_track += 1
        except IndexError:  # no coins // exceeds list index
            return -1
    return count
