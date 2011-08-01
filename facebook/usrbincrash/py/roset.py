#!/usr/bin/python
from itertools import product, izip
from collections import namedtuple
 
Bounty = namedtuple('Bounty', 'name value weight volume')
 
sack =   Bounty('sack',       0, 250, 250)
 
items = [Bounty('panacea', 3000,   3,  25),
         Bounty('ichor',   1800,   2,  15),
         Bounty('gold',    2500,  20,   2)]
 
 
def tot_value(items_count, items, sack):
    """
    Given the count of each item in the sack return -1 if they can't be carried or their total value.
 
    (also return the negative of the weight and the volume so taking the max of a series of return
    values will minimise the weight if values tie, and minimise the volume if values and weights tie).
    """
    weight = sum(n * item.weight for n, item in izip(items_count, items))
    volume = sum(n * item.volume for n, item in izip(items_count, items))
    if weight <= sack.weight and volume <= sack.volume:
        return sum(n * item.value for n, item in izip(items_count, items)), -weight, -volume
    else:
        return -1, 0, 0
 
 
def knapsack_dp(items, sack):
    """
    Solves the Knapsack problem, with two sets of weights,
    using a dynamic programming approach
    """
    # (weight+1) x (volume+1) table
    # table[w][v] is the maximum value that can be achieved
    # with a sack of weight w and volume v.
    # They all start out as 0 (empty sack)
    table = [[0] * (sack.volume + 1) for i in xrange(sack.weight + 1)]
 
    for w in xrange(sack.weight + 1):
        for v in xrange(sack.volume + 1):
            # Consider the optimal solution, and consider the "last item" added
            # to the sack. Removing this item must produce an optimal solution
            # to the subproblem with the sack's weight and volume reduced by that
            # of the item. So we search through all possible "last items":
            for item in items:
                # Only consider items that would fit:
                if w >= item.weight and v >= item.volume:
                    table[w][v] = max(table[w][v],
                                      # Optimal solution to subproblem + value of item:
                                      table[w - item.weight][v - item.volume] + item.value)
 
    # Backtrack through matrix to re-construct optimum:
    result = [0] * len(items)
    w = sack.weight
    v = sack.volume
    while table[w][v]:
        # Find the last item that was added:
        aux = [table[w-item.weight][v-item.volume] + item.value for item in items]
        i = aux.index(table[w][v])
 
        # Record it in the result, and remove it:
        result[i] += 1
        w -= items[i].weight
        v -= items[i].volume
 
    return result
 
 
max_items = knapsack_dp(items, sack)
max_value, max_weight, max_volume = tot_value(max_items, items, sack)
max_weight = -max_weight
max_volume = -max_volume
 
print "The maximum value achievable (by exhaustive search) is %g." % max_value
item_names = ", ".join(item.name for item in items)
print "  The number of %s items to achieve this is: %s, respectively." % (item_names, max_items)
print "  The weight to carry is %.3g, and the volume used is %.3g." % (max_weight, max_volume)
