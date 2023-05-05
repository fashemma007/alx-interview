#!/usr/bin/python3
"""module docs for 0-minoperations.py"""


def minOperations(n):
    """Returns an integer"""
    if n <= 1:
        return 0
    dp = [0] * (n + 1)
    # print(dp)
    for i in range(2, n + 1):
        dp[i] = i
        # print(dp)
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                dp[i] = dp[j] + (i // j)
                break
    return dp[n]
