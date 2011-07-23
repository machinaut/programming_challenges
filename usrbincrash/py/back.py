#!/usr/bin/python
from itertools import product, izip
from collections import namedtuple
from math import ceil
 
Bounty = namedtuple('Bounty', 'name weight value')
 
sack =   Bounty('sack',     12,      0)
 
items = [Bounty('LJS93K',   13,   11),
         Bounty('J38ZZ9',   7,    5),
         Bounty('HJ394L',   2,    3),
         Bounty('O1IE82',   1,     10)]

best = items[1]

#TODO:
#Add dominances and common sense limits
 
def knapsack_dp(items, sack):
    """
    Solves the Knapsack problem, with a given weights and values
    using a dynamic programming approach
    """
    table = [0] + [None] * (sack.weight + 13)
    for w in xrange(1,sack.weight + 14):
        print 'w =', w
        for item in items:
            print 'item w,v:', item.weight, item.value
            if w > item.weight:
                print 'item.w < w', item.weight, w
                if table[w] is None:
                    table[w] = table[w - item.weight] + item.value
                    print 'table[%d] was None, now is' % w, table[w]
                else:
                    print 'table[%d] was'%w,table[w],' now is', table[w - item.weight] + item.value
                    table[w] = min(table[w], table[w - item.weight] + item.value)
            print table 

    return table[sack.weight]
 
 
print knapsack_dp(items, sack)
 
