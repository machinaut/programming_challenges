#!/usr/bin/env python
import sys

def brute(bag, items):
    """
    Brute force solution to the inverse unbounded knapsack problem
    finds the minimum cost to dump bag amount of weight using items
    """
    r = reduce(lambda a,(w,c,m):a*m, items, 1)
    best = None # best cost solution
    for i in xrange(r): # for each possible solution
        totalweight, totalcost = 0, 0
        for weight, cost, max in items:
            qty, i = i % max, i / max
            totalweight, totalcost = qty*weight+totalweight, qty*cost+totalcost
        if totalweight >= weight and (best is None or totalcost < best):
            best = totalcost
    return best

def dynamic(bag, items):
    """
    Solves the Knapsack problem, with a given weights and values
    using a dynamic programming approach
    """
    table = [0] + [None] * (bag)
    for w in xrange(1,bag):
        print 'w =', w
        for item in items:
            print 'item w,v:', item.weight, item.value
            if w > item.weight:
                print 'item.w < w', item.weight, w
                if table[w] is None:
                    table[w] = table[w - item.weight] + item.value
                else:
                    table[w] = min(table[w], table[w - item.weight] + item.value)
            print table 
    return table[sack.weight]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'usage: ./brute.py <inputfile>'
        exit(1)

    input = open(sys.argv[1]) # input file
    bag = int(input.readline().strip()) # max weight we have to drop

    items = [] #(weight, cost, max), ...

    for line in input:
        SKU, weight, cost = line.split()
        max = (bag + int(weight) - 1)/ int(weight) + 1 # max qty of this item
        items.append( (int(weight), int(cost), max) )
    print bag
    print items
    print brute(bag, items) 
