#!/usr/bin/env python
import sys

def brute(bag, items):
    """
    Brute force solution to the inverse unbounded knapsack problem
    finds the minimum cost to dump bag amount of weight using items
    """
    best = None # best cost solution
    for i in xrange(reduce(lambda a,(w,c,m):a*m, items, 1)):
        totalweight, totalcost = 0, 0
        for weight, cost, max in items:
            qty, i = i % max, i / max
            totalweight += qty * weight
            totalcost += qty * cost
        if totalweight >= bag and (best is None or totalcost < best):
            best = totalcost
    return best

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

    print brute(bag, items) 

