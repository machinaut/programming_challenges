#!/usr/bin/python
from itertools import product, izip
from collections import namedtuple
 
Bounty = namedtuple('Bounty', 'name value weight')
 
sack =   Bounty('sack',       0, 250)
 
items = [Bounty('panacea', 3000,   3),
         Bounty('ichor',   1800,   2),
         Bounty('gold',    2500,  20)]

"""
TODO:
Add dominances and common sense limits
"""
 
 
def tot_value(items_count, items, sack):
    """
    Given the count of each item in the sack return -1 if they can't be carried or their total value.
 
    (also return the negative of the weight and the volume so taking the max of a series of return
    values will minimise the weight if values tie, and minimise the volume if values and weights tie).
    """
    weight = sum(n * item.weight for n, item in izip(items_count, items))
    if weight <= sack.weight:
        return sum(n * item.value for n, item in izip(items_count, items)), -weight
    else:
        return -1, 0, 0
 
 
def knapsack_dp(items, sack):
    """
    Solves the Knapsack problem, with two sets of weights,
    using a dynamic programming approach
    """
    table = [0] * (sack.weight + 1)
    for w in xrange(sack.weight + 1):
        for item in items:
            if w >= item.weight:
                table[w] = max(table[w], table[w - item.weight] + item.value)
 
    return table[sack.weight]
 
 
print knapsack_dp(items, sack)
 
