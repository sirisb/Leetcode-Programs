"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
ith customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is
the customer that has the maximum wealth.
"""
import numpy as np


# Using nparray.
def max_wealth(accounts_list) -> int:
    if len(accounts_list) < 1:
        return 0
    return (np.sum(np.array(accounts_list), axis=1)).max()


def max_wealth1(accounts_list):
    max_bal = 0
    for row in accounts_list:
        max_bal = max(sum(row), max_bal)
    print(max_bal)


if __name__ == "__main__":
    accounts = [[1, 2, 3], [3, 4, 1], [4, 6, 1]]
    print(max_wealth(accounts))
    max_wealth1(accounts)
